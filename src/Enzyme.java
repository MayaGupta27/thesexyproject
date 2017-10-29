public class Enzyme {
	public double efficiency;
	public String name;
	public int noOfRs;
	public Reaction[] reactions;
	
	//constructor
	public Enzyme(String newName, double newEfficiency, Reaction[] newReactions) {
		this.name = newName;
		this.efficiency = newEfficiency;
		this.reactions = newReactions;	
	}
	
	//iterates through list of reactions and completes them one at a time
	public static void doEnzyme(Enzyme enzyme) {
		while (true) {
			for (int i = 0; i < enzyme.Reaction[].length; i++) {
				enzyme.doReaction(Reaction[i]);
			}
		}
	}
	
	private static double getEfficiency(RsNumber... numbers) {
	     double total = 0.0;
	     double count = 0.0;
	     for (int rsNumber : numbers) {
	    	 	total = total + rsNumber.getRSStatus( , , );
	    	 	count++;
	     }
	     double efficiency = total / count;
	     return efficiency;
	}
	
	
}