public class Reaction {
	Hormone product;
	Hormone reactant;
	
	//constructor
	public Reaction(Hormone newReactant, Hormone newProduct) {
		this.product = newProduct;
		this.reactant = newReactant;
	}
	
	// converts one unit of product to one unit of reactant.
	public void doReaction() {
		product.amount = product.amount + 1;
		reactant.amount = reactant.amount - 1;
		Hormone.updateColour(product);
		Hormone.updateColour(reactant);
	}
	
}