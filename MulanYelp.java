package classification;

import java.io.FileReader;
import java.io.PrintWriter;

import mulan.classifier.MultiLabelOutput;
import mulan.classifier.lazy.MLkNN;
import mulan.classifier.meta.RAkEL;
import mulan.classifier.transformation.LabelPowerset;
import mulan.data.MultiLabelInstances;
import mulan.evaluation.Evaluator;
import mulan.evaluation.MultipleEvaluation;
import weka.classifiers.trees.J48;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.Utils;

public class MulanYelp {
	public static void main(String[] args) {
		try {
			// **** GET TRAINING DATA
			PrintWriter writer = new PrintWriter("results2.txt", "UTF-8");
			
			String[] arff = {"-arff","dataset.arff"};
            String trainarff = Utils.getOption("arff", arff);
            String[] xml = {"-xml","dataset.xml"};
            String trainxml = Utils.getOption("xml", xml);
			
			MultiLabelInstances dataset = new MultiLabelInstances(trainarff, trainxml);
			
			// **** TRAINING CLASSIFICATION ALGORITHMS
			RAkEL learner1 = new RAkEL(new LabelPowerset(new J48()));
			MLkNN learner2 = new MLkNN();
			
			// **** GET PREDICTIONS
//			learner1.build(dataset);
//			learner2.build(dataset);

//			String[] testarff = {"-arff","test-dataset.arff"};
//			String unlabeledFilename = Utils.getOption("arff", testarff);
//			FileReader reader = new FileReader(unlabeledFilename);
//			Instances unlabeledData = new Instances(reader);
//			
//			int numInstances = unlabeledData.numInstances();
//
//			writer.print("business_id,labels");
//			for (int instanceIndex=0; instanceIndex < numInstances; instanceIndex++) {
//				Instance instance = unlabeledData.instance(instanceIndex);
//				MultiLabelOutput output = learner1.makePrediction(instance);
//				// do necessary operations with provided prediction output, here just print it out
//				System.out.println(output);
//				for(int i=0;i<9;i++){
//					if(output.getBipartition()[i])
//						writer.print((i+1) + " ");
//				}
//				writer.print("\n");
//			}
//
//			writer.close();
			
			// **** GET EVALUATIONS
			Evaluator eval = new Evaluator();
			MultipleEvaluation results;
			
			int numFolds = 10;
			results = eval.crossValidate(learner1, dataset, numFolds);
			System.out.println(results);
			results = eval.crossValidate(learner2, dataset, numFolds);
			System.out.println(results);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	
	
}
