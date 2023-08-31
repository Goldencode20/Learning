package SimpleAITest;

import java.util.ArrayList;
import java.util.List;


public class Node {
    private List<Double> weights;
    private double bias, output, error;
    private double learningRate = 0.1;

    public Node(int inputSize) {
        weights = new ArrayList<>();
        for (int i = 0; i < inputSize; i++) {
            double weight = Math.random();
            if (Math.random() < 0.5) { weight = weight - 1; }
            weights.add(weight); //Set up with random weights
        }
        bias = Math.random(); //set up with random bias
    }

    public double calculateOutput(List<Double> inputs, int function) {
        if (inputs.size() != weights.size()) {
            throw new IllegalArgumentException("Input size doesn't match the number of weights.");
        }

        double sum = bias;
        for (int i = 0; i < inputs.size(); i++) {
            sum += inputs.get(i) * weights.get(i);
        }

        //I can chagne the function here
        switch (function) {
            case 1: output = sigmoid(sum);
                    break;
            case 2: if(sum > 0) { output = 1.0; }
                    else { output = 0; }
                    break;
            case 3: output = Math.tanh(sum);
                    break;
            case 4: output = Math.max(0, sum);
                    break;
        }
        return output;
    }

    private double sigmoid(double x) {
        return 1.0 / (1.0 + Math.exp(-x));
    }

    public double getOutput() {
        return output;
    }

    public void updateWeights(List<Double> inputs, double error) {
        if (inputs.size() != weights.size()) {
            throw new IllegalArgumentException("Input size doesn't match the number of weights.");
        }

        double deltaBias = learningRate * error * output * (1.0 - output);
        bias += deltaBias;

        for (int i = 0; i < weights.size(); i++) {
            double deltaWeight = learningRate * error * inputs.get(i) * output * (1.0 - output);
            weights.set(i, weights.get(i) + deltaWeight);
        }
        this.error = error;
    }

    public List<Double> getWeights() {
        return weights;
    }

    public double getError() {
        return error;
    }
}
