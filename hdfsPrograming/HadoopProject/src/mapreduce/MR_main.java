package mapreduce;

import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

import mapreduce.MapReducer.My_Map;
import mapreduce.MapReducer.My_Reduce;

public class MR_main {

	public static void main(String[] args) throws IOException {
		JobConf job = new JobConf(MapReducer.class);
		
		job.setJobName("MR_Test");
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.setMapperClass(My_Map.class);
		job.setCombinerClass(My_Reduce.class);
		job.setReducerClass(My_Reduce.class);
		
		job.setInputFormat(TextInputFormat.class);
		job.setOutputFormat(TextOutputFormat.class);
		
		FileInputFormat.setInputPaths(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		
		JobClient.runJob(job);
	}

}
