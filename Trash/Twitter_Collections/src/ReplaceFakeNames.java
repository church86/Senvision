import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ReplaceFakeNames {

	public static void fixFile(File fileToChange,String outputfile) throws IOException{
		BufferedReader bR = new BufferedReader(new FileReader(fileToChange));
		BufferedWriter bW = new BufferedWriter(new FileWriter(outputfile));
		
		String nextLine;
		while((nextLine=bR.readLine())!=null){
			bW.write(nextLine.replace("^", "")+"\n");
		}
		bR.close();
		bW.close();
	}
	
	
	public static void showFiles(File[] files) {
	    for (File file : files) {
	        if (file.isDirectory()) {
	            System.out.println("Directory: " + file.getName());
	            File newDir = new File("/home/mankeyace/GitHub/stock/replacedTweets/"+file.getName());
	            newDir.mkdir();
	            showFiles(file.listFiles()); // Calls same method again.
	        } else {
	            try {
					fixFile(file,"/home/mankeyace/GitHub/stock/replacedTweets/"+file.getParent().substring(file.getParentFile().toString().lastIndexOf("/"))+"/"+file.getName());
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	        }
	    }
	}
	public static void main(String[] args){
		File TweetsFolder = new File("/home/mankeyace/GitHub/stock/Tweets");
		File[] TweetsArray = TweetsFolder.listFiles();
		showFiles(TweetsArray);
	}
	
}