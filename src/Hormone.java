//this will make a hormone object, or coloured square

public class Hormone {
	int colour;
	String name;
	int amount; 

	//constructor
	public Hormone(String newName) {
		this.name = newName;
		this.amount = 0;
	}
	
	
	public static int MIN_AMOUNT = 0;
	public static int MIN_COLOUR = 0xFF000000;
	public static int LVL1_AMOUNT = 20;
	public static int LVL1_COLOUR = 0xFFFF0000;
	public static int LVL2_AMOUNT = 40;
	public static int LVL2_COLOUR = 0xFF00FF00;
	public static int LVL3_AMOUNT = 60;
	public static int LVL3_COLOUR = 0xFF0000FF;
	
	//sets the colour. Should be called any time the amount is changed.
	public static void updateColour(Hormone hormone) {
		if (hormone.amount >= MIN_AMOUNT && (hormone.amount < LVL1_AMOUNT)) {
			hormone.colour = MIN_COLOUR;
		} else if (hormone.amount >= LVL1_AMOUNT && hormone.amount < LVL2_AMOUNT) {
			hormone.colour = LVL1_COLOUR;	
		} else if (hormone.amount >= LVL2_AMOUNT && hormone.amount < LVL3_AMOUNT) {
			hormone.colour = LVL2_COLOUR;
		} else {
			hormone.colour = LVL3_COLOUR;
		}
	}
}