import java.io.*;
import java.util.LinkedHashSet;
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

  static LinkedHashSet<String> dict = new LinkedHashSet();

  public static class TokenizeMapper 
  extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private final static IntWritable two = new IntWritable(2);
    private Text word = new Text();
  
    public void map(Object Key, Text value, Context context
    ) throws IOException, InterruptedException {
      //Substring to skip the b character
      StringTokenizer itr = new StringTokenizer(
        value.toString().substring(2));
      while(itr.hasMoreTokens()){
        word.set(itr.nextToken());
        String w = word.toString();
        if(!isLink(w)){
          w = w.replaceAll("[^a-zA-Z ]", "").toLowerCase();
          if(dict.contains(w)){
            context.write(new Text(w),one);
          } else {
            if(!w.equals("")){
              context.write(new Text(w),two);
            }
          }
        }
      }
    }

    //Checks if the file is a link.
    public static boolean isLink(String word){
      return (word.charAt(0) == '#' || word.charAt(0) == '@'
        || word.contains("http")
        || word.charAt(0)=='&'|| word.contains("\\"));
    }
  }

  public static class SmallReducer 
  extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
    throws IOException, InterruptedException {
      context.write(key, values.iterator().next());
    }
  }

  public static void main(String[] args) 
  throws IOException, InterruptedException, ClassNotFoundException {
    
    BufferedReader br = new BufferedReader
    (new FileReader(System.getProperty("user.dir")+"/words"));
    String str;
    while ((str = br.readLine()) != null) {
      dict.add(str.toLowerCase());
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