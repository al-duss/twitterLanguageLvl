import java.io.*;
import java.util.HashSet;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class wordCount {

  static HashSet<String> dict = new HashSet();
  final static IntWritable one = new IntWritable(1);
  final static IntWritable zero = new IntWritable(0);

  public static class TokenizeMapper 
  extends Mapper<Object, Text, Text, IntWritable>{

    final static IntWritable one = new IntWritable(1);
    final static IntWritable zero = new IntWritable(0);
    private Text word = new Text();
  
    public void map(Object Key, Text value, Context context
    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while(itr.hasMoreTokens()){
        word.set(itr.nextToken());
        String x = word.toString();
        if(!isLink(x)){
          //Check for unicode characters or punctuation, if in middle of word, seperate into two.
          x = x.replaceAll("\\\\U[a-f0-9]{8}|\\\\u[a-f0-9]{4}|\\\\n|\\\\t|[\\[\\](){},.;!?<>%]"," ");
          String[] parts = x.split(" ");
          //Remove Non-letters, as well as unicode characters
          for (String w: parts){
            w = w.replaceAll("[^a-zA-Z']", "").toLowerCase();
            if(dict.contains(w)){
              context.write(new Text(w),one);
            } else {
              if(!w.equals("")){
                context.write(new Text(w),zero);
              }
            }
          }
        }
      }
    }

    //Checks if the word is a link or should be ignored.
    public static boolean isLink(String word){
      return (word.contains("#") || word.contains("@")
        || word.contains("http") || word.contains("&"));
    }
  }

  public static class SmallReducer 
  extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context)
    throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val: values){
        sum += val.get();
      }   
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) 
  throws IOException, InterruptedException, ClassNotFoundException {
    
    //Accessing the built-in linux dictionary
    BufferedReader br = new BufferedReader
    (new FileReader(System.getProperty("user.dir")+"/words"));
    String str;
    while ((str = br.readLine()) != null) {
      String w = str.toLowerCase();
      dict.add(w);
    }
    br.close();

    Configuration conf = new Configuration();
    Job job1 = Job.getInstance(conf, "word count");
    job1.setJarByClass(wordCount.class);
    job1.setMapperClass(TokenizeMapper.class);
    job1.setReducerClass(SmallReducer.class);
    job1.setOutputKeyClass(Text.class);
    job1.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job1, new Path(args[0]));
    FileOutputFormat.setOutputPath(job1, new Path(args[1]));
    System.exit(job1.waitForCompletion(true) ? 0 : 1);
  }
}