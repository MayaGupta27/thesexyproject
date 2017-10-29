public class RsNumber {
	String rsNumber;
	char riskAllele;
	char allele1;
	char allele2;
	double rSStatus;
	
	//constructor
	public RsNumber(String newrsNumber, char newRiskAllele, char newAllele1, char newAllele2) {
		this.rsNumber = newrsNumber;
		this.riskAllele = newRiskAllele;
		this.allele1 = newAllele1;
		this.allele2 = newAllele2;
		this.rSStatus = getRSStatus(riskAllele, allele1, allele2);
	}
	
	/**
	 * compares alleles 1 and 2 with the risk allele and determines the status of the rsNumber
	 * @param riskAllele
	 * @param allele1
	 * @param allele2
	 * @return double rs efficiency. Should always be 0, 0.5 or 1.
	 */
	public double getRSStatus(char riskAllele, char allele1, char allele2) {
		double rSStatus = 1;
		boolean risk1 = allele1 == riskAllele;
		boolean risk2 = allele2 == riskAllele;
		if (risk1 && risk2) {
			rSStatus = 0;
		} else if (risk1 != risk2) {
			rSStatus = 0.5;
		} else {
			rSStatus = 1;
		}
		return rSStatus;
	}
	
}