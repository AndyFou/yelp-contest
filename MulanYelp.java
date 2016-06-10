/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mulanyelp;

/**
 *
 * @author user
 */
import weka.classifiers.Evaluation;
import weka.core.Utils;
import mulan.data.MultiLabelInstances;
import mulan.classifier.lazy.MLkNN;
import mulan.classifier.meta.RAkEL;
import mulan.classifier.transformation.LabelPowerset;
import weka.classifiers.trees.J48;
import mulan.evaluation.Evaluator;
import mulan.evaluation.MultipleEvaluation;



public class MulanYelp {
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            //GET DATA
            String[] arff = {"-arff","dataset.arff"};
            String arfffile = Utils.getOption("arff", arff);
            String[] xml = {"-xml","dataset.xml"};
            String xmlfile = Utils.getOption("xml", xml);
            
            MultiLabelInstances dataset = new MultiLabelInstances(arfffile, xmlfile);
            
            //TRAIN LEARNERS
            RAkEL learner1 = new RAkEL(new LabelPowerset(new J48()));
            MLkNN learner2 = new MLkNN();
            
            Evaluator eval = new Evaluator();
            MultipleEvaluation results;
            
            //EVALUATE RESULTS
            int numFolds = 10;
            results = eval.crossValidate(learner1, dataset, numFolds);
            System.out.println(results);
            results = eval.crossValidate(learner2, dataset, numFolds);
            System.out.println(results);
        }
        catch(Exception e){
            System.out.println(e);
        }
        
        
        
    }
    
}
