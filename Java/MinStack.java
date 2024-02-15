class MinStack {

    private Object minValue;
    private MinStack stack;

    public MinStack() {
        int[] minValue;
        Stack<Integer> stack = new Stack<Integer>();
    }
    
    public void push(int val) {
        for(int x = 0; x < minValue.length(); x++) {
            minValue.add(val);
            stack.push(val);
        }
    }
    
    public void pop() {
        minValue = Arrays.copyOf(minValue, minValue.length() - 1);
        stack.pop();
    }
    
    public int top() {
        return stack.top();
    }
    
    public int getMin() {
        return Collections.min(Arrays.asList(num));
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */