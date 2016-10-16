import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

public class TweetStockDataPairer {
	public static void createPair(String StockFile, String DescriptorFile, String XValFile) throws IOException {
		Map<String, String> stockupdown = new HashMap<String, String>();
		CSVReader StockReader = new CSVReader(new FileReader(StockFile),'\t');
		CSVWriter XValWriter = new CSVWriter(new FileWriter(XValFile));
		CSVWriter KnimeInputWriter = new CSVWriter(new FileWriter("../../KnimeInput/Knimeinput.tsv",true),'\t');
		CSVReader DescriptorReader = new CSVReader(new FileReader(DescriptorFile), '\t');
		//StockReader.readNext();
		//DescriptorReader.readNext();
		String[] readDesLine;
		String[] readStockLine;
		
		
		while ((readStockLine = StockReader.readNext()) != null) {
			readDesLine = DescriptorReader.readNext();
			stockupdown.put(readStockLine[1], readStockLine[readStockLine.length - 2]);
			System.out.println(
					"Stock date: " + readStockLine[1] + "   Stock up down: " + readStockLine[readStockLine.length - 2]);
		}
		
		String writeLine[];
		StockReader.close();
		DescriptorReader.close();
		DescriptorReader = new CSVReader(new FileReader(DescriptorFile), '\t');
		readDesLine = DescriptorReader.readNext();
		writeLine = new String[readDesLine.length];
		for (int i = 0; i < readDesLine.length-1; i++) {
			writeLine[i] = readDesLine[i];
		}
		writeLine[readDesLine.length-1] = "+/-/=";
		XValWriter.writeNext(writeLine);
		
		while ((readDesLine = DescriptorReader.readNext()) != null) {

			if (stockupdown.containsKey(readDesLine[0])) {
				for (int i = 0; i < readDesLine.length-1; i++) {
					writeLine[i] = readDesLine[i];
				}
				writeLine[readDesLine.length-1] = stockupdown.get(readDesLine[0]);
				XValWriter.writeNext(writeLine);
				KnimeInputWriter.writeNext(writeLine);
			}

		}

		DescriptorReader.close();
		XValWriter.close();
		KnimeInputWriter.close();
	}

	public static void createPairsFolders(String DescriptorFolder, String StockFolder, String XValOutputFolder) {
		for (File DescriptorFile : new File(DescriptorFolder).listFiles()) {
			System.out.println("Compnay: "+DescriptorFile.getName());
			try {
				System.out.println("asdfawefawgafja;odf;aijsdf;iasdfij;");
				createPair(StockFolder + "/" + DescriptorFile.getName().substring(0, DescriptorFile.getName().indexOf("_"))
								+ "_cleaned.csv", 
						DescriptorFile.getPath(), XValOutputFolder + "/" + DescriptorFile.getName().substring(0,DescriptorFile.getName().indexOf(".tsv"))+".csv");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args) {
		createPairsFolders("../../descriptors", "../../stock_data/tweet_date_data", "../../XValSets");
		System.out.println("what the fuckk");
		System.out.println("wadsfwefwatwefaoiweofoawf");
	}
}