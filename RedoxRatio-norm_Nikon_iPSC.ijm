

dir = getDirectory("Choose a Directory ");

 
filename=File.openDialog("Select a File"); //Selection of individual image
filebasewithext = File.getName(filename);
filebase = substring(filebasewithext, 0, lastIndexOf(filebasewithext, "."));
open(filename);

run("Subtract Background...", "rolling=250");
setAutoThreshold("Default dark");
//run("Threshold...");
setOption("BlackBackground", false);
run("Convert to Mask");
run("Divide...", "value=255.000");
run("Measure Stack...");

 

// Puts all the measurements for this stack into an array

              Pixelcountmask =  getResult("RawIntDen");

              
saveAs("Tiff",dir+ File.separator + File.separator +filebase+"mask"+".tif");

                      
NADHfile=File.openDialog("Select a File"); //Select N raw image
open(NADHfile);

selectWindow(filebase+".tif");
imageCalculator("Multiply create 32-bit", filebase+"mask"+".tif", filebase+".tif");
saveAs("Tiff",dir+ File.separator + File.separator +filebase+"masked"+".tif");
run("Measure Stack...");
			IntensityN=getResult("Mean")

FADfile=File.openDialog("Select a File"); //Select F raw image
open(FADfile);
filebasewithextFAD = File.getName(FADfile);
filebaseFAD = substring(filebasewithextFAD, 0, lastIndexOf(filebasewithextFAD, "."));

selectWindow(filebaseFAD+".tif");
imageCalculator("Multiply create 32-bit", filebase+"mask"+".tif", filebaseFAD+".tif");
saveAs("Tiff",dir+ File.separator + File.separator +filebaseFAD+"masked"+".tif");
run("Measure Stack...");
			IntensityF=getResult("Mean")

imageCalculator("Add create 32-bit", filebase+"masked"+".tif", filebaseFAD+"masked"+".tif");
saveAs("Tiff",dir+ File.separator + File.separator +filebase+"sum"+".tif");

imageCalculator("Divide create 32-bit", filebase+"masked"+".tif", filebase+"sum"+".tif");
run("Measure Stack...");

// Puts all the measurements for this stack into an array
			PixelcountRR=getResult("RawIntDen");
			MeanRR=PixelcountRR/Pixelcountmask;
			print(MeanRR,",", IntensityN, ",", IntensityF);
			
run("Close All");