public class TheSexyProject {
	public static void main(String[] args) {
		//String[] rsCOMT = {rs6270, rs6267, rs5031015, rs4986871, rs4680};
		//Enzyme COMT = new Enzyme("COMT", getEfficiency(rsCOMT), 2hydroxyEstrone, 2methoxyEstrone);
		Hormone twoHydroxyEstrone = new Hormone("2 hydroxy estrone");
		Hormone twoMethoxyEstrone = new Hormone("2 methoxy estrone");
		Hormone fourHydroxyEstrone = new Hormone("4 hydroxy estrone");
		Hormone fourMethoxyEstrone = new Hormone("4 methoxy estrone");
		Hormone estrone = new Hormone("estrone");
		Hormone sixteenAlphaHydroxyEstrone = new Hormone("16 alpha hydroxy estrone");
		Hormone estradiol = new Hormone("estradiol");
		Hormone estriol = new Hormone("estriol");
		Hormone cholesterol = new Hormone("cholesterol");
		Hormone pregnenolone = new Hormone("pregnenolone");
		Hormone seventeenAlphaHydroxyPregnenolone = new Hormone("17 alpha hydroxy pregnenolone");
		Hormone progesterone = new Hormone("progesterone");
		Hormone seventeenAlphaHydroxyProgesterone = new Hormone("17 alpha hydroxy progesterone");
		Hormone dHEA = new Hormone("DHEA");
		Hormone dHEAS = new Hormone("DHEA-S");
		Hormone androstenedione = new Hormone("androstenedione");
		Hormone testosterone = new Hormone("Testosterone");
		Hormone seventeenBetaEstradiol = new Hormone("17 beta estradiol");
		Hormone deoxyCorticosterone = new Hormone("deoxy corticosterone");
		Hormone elevenDeoxyCortisol = new Hormone("11 deoxy cortisol");
		Hormone androstadienone = new Hormone("androstadienone");
		Hormone androstenediol = new Hormone("androstenediol");
		Hormone androstadienol = new Hormone("androstadienol");
		
		Reaction tHEtME = new Reaction(twoHydroxyEstrone, twoMethoxyEstrone);
		Reaction fHEfME = new Reaction(fourHydroxyEstrone, fourMethoxyEstrone);
		Reaction estronetHE = new Reaction(estrone, twoHydroxyEstrone);
		Reaction estronefHE = new Reaction(estrone, fourHydroxyEstrone);
		Reaction estronesAHE = new Reaction(estrone, sixteenAlphaHydroxyEstrone);
		Reaction estradiolEstriol = new Reaction(estradiol, estriol);
		Reaction cholesterolPregnenolone = new Reaction(cholesterol, pregnenolone);
		Reaction pregnenolonesAHP = new Reaction(pregnenolone, seventeenAlphaHydroxyPregnenolone);
		Reaction progesteronesAHP = new Reaction(progesterone, seventeenAlphaHydroxyPregnenolone);
		Reaction sAHPDHEA = new Reaction(seventeenAlphaHydroxyPregnenolone, dHEA);
		Reaction sAHPAndrostenedione = new Reaction(seventeenAlphaHydroxyProgesterone, androstenedione);
		Reaction androstenedioneEstrone = new Reaction(androstenedione, estrone);
		Reaction testosteronesBE = new Reaction(testosterone, seventeenBetaEstradiol);
		Reaction progesteroneDeoxyCorticosterone = new Reaction(progesterone, deoxyCorticosterone);
		Reaction sAHPeDC = new Reaction(seventeenAlphaHydroxyProgesterone, elevenDeoxyCortisol);
		Reaction testosteroneAndrostenedione = new Reaction(testosterone, androstenedione);
		Reaction pregnenoloneProgesterone = new Reaction(pregnenolone, progesterone);
		Reaction sAHPsAHP = new Reaction(seventeenAlphaHydroxyPregnenolone, seventeenAlphaHydroxyProgesterone);
		Reaction dHEAAndrostenedione = new Reaction(dHEA, androstenedione);
		Reaction androstenediolTestosterone = new Reaction(androstenediol, testosterone);
		Reaction androstadienolAndrostadienone = new Reaction(androstadienol, androstadienone);
		Reaction sBEEstrone = new Reaction(seventeenBetaEstradiol, estrone);
		Reaction dHEAdHEAS = new Reaction(dHEA, dHEAS);
		
		
		
		
		//Reaction 2hydroxyestrone_2methoxyestrone = new Reaction(2hydroxyestrone, 2methoxyestrone);
		//String[] rsCYP3A4 = {rs12721634, rs56324128};
		//Enzyme CYP3A4 = new Enzyme("CYP3A4", getEfficiency(rsCYP3A4));	
	}
}