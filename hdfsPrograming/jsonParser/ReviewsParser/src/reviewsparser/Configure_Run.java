package reviewsparser;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

//import com.sun.jersey.core.impl.provider.entity.XMLJAXBElementProvider.Text;

public class Configure_Run {

	public static String json = null;
	
	public static void getData(String jsonData) {
		json = jsonData;
	}
	
	public static void main(String[] args) throws Exception, IOException{

		//adding JDK path to pom.xml!
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "TestJob");
		
		job.setJarByClass(MapReducerTest.class);
		job.setMapperClass(MapReducerTest.ReviewerMap.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		//FileInputFormat.addInputPath(job, new Path("../ReviewsParser/sample/reviews_sample.txt"));
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		
		job.waitForCompletion(true);
		
		System.exit(0);
	}
	
	
}
