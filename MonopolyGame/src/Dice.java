public class Dice {
	private int faceValue;
	public int rollDice() {
		int newFaceValue=(int)(Math.random()*6+1);
		setFaceValue(newFaceValue);
		System.out.println("Face Value of dice is: "+newFaceValue+".");
		return newFaceValue;
	}
	/**
	 * @return the faceValue
	 */
	public int getFaceValue() {
		return faceValue;
	}
	/**
	 * @param faceValue the faceValue to set
	 */
	public void setFaceValue(int faceValue) {
		this.faceValue = faceValue;
	}
}