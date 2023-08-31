package SimpleAITest;

import java.util.ArrayList;
import java.util.List;

public class NeuralNetwork {
    private List<List<Node>> layers;

    public NeuralNetwork(int... layerSizes) {
        if (layerSizes.length < 2) {
            throw new IllegalArgumentException("At least two layers are required.");
        }

        layers = new ArrayList<>();
        for (int i = 0; i < layerSizes.length; i++) {
            List<Node> layer = new ArrayList<>();
            int numNodes = layerSizes[i];
            int numInputs = (i == 0) ? layerSizes[0] : layerSizes[i - 1]; // Number of nodes in previous layer

            for (int j = 0; j < numNodes; j++) {
                layer.add(new Node(numInputs));
            }

            layers.add(layer);
        }
    }

    public List<Double> predict(List<Double> inputs) {
        List<Double> currentInputs = new ArrayList<>(inputs);

        for (List<Node> layer : layers) {
            List<Double> newInputs = new ArrayList<>();
            for (Node node : layer) {
                newInputs.add(node.calculateOutput(currentInputs, 1)); //Change the function here 
            }
            currentInputs = newInputs;
        }

        return currentInputs;
    }

    public void train(List<List<Double>> inputSamples, List<List<Double>> targetOutputs, int epochs) {
        for (int epoch = 0; epoch < epochs; epoch++) {
            for (int sampleIndex = 0; sampleIndex < inputSamples.size(); sampleIndex++) {
                List<Double> input = inputSamples.get(sampleIndex);
                List<Double> targetOutput = targetOutputs.get(sampleIndex);

                List<Double> predictedOutput = predict(input);

                for (int layerIndex = layers.size() - 1; layerIndex >= 0; layerIndex--) {
                    List<Node> layer = layers.get(layerIndex);
                    List<Double> layerInputs = (layerIndex == 0) ? input : layers.get(layerIndex - 1).stream().map(Node::getOutput).toList();
                    for (int nodeIndex = 0; nodeIndex < layer.size(); nodeIndex++) {
                        double error = (layerIndex == layers.size() - 1)
                                       ? targetOutput.get(nodeIndex) - predictedOutput.get(nodeIndex)
                                       : calculateHiddenNodeError(layerIndex, nodeIndex);
                        layer.get(nodeIndex).updateWeights(layerInputs, error);
                    }
                }
            }
        }
    }

    private double calculateHiddenNodeError(int layerIndex, int nodeIndex) {
        double sum = 0.0;
        for (Node nextLayerNode : layers.get(layerIndex + 1)) {
            sum += nextLayerNode.getWeights().get(nodeIndex) * nextLayerNode.getError();
        }
        return sum;
    }
}