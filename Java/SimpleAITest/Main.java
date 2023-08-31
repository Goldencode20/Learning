package SimpleAITest;

import java.util.List;

    public class Main {
     public static void main(String[] args) {
        NeuralNetwork neuralNetwork = new NeuralNetwork(2, 2, 1);

        List<List<Double>> inputSamples = List.of(
                List.of(0.0, 0.0),
                List.of(0.0, 1.0),
                List.of(1.0, 0.0),
                List.of(1.0, 1.0)
        );

        List<List<Double>> targetOutputs = List.of(
                List.of(0.0),
                List.of(1.0),
                List.of(1.0),
                List.of(0.0)
        );

        neuralNetwork.train(inputSamples, targetOutputs, 10000);

        for (List<Double> input : inputSamples) {
            List<Double> output = neuralNetwork.predict(input);
            System.out.println("Input: " + input + ", Predicted Output: " + output);
        }
    }
}