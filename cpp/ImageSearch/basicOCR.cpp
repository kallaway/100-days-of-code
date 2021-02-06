#include "basicOCR.h"
 
using namespace std;
using namespace cv;
 
string getText(string imagePath)
{
	string outText;
 
    Mat im = cv::imread(imagePath, IMREAD_COLOR);
	
	tesseract::TessBaseAPI *ocr = new tesseract::TessBaseAPI();
     
    ocr->Init(NULL, "eng", tesseract::OEM_LSTM_ONLY);
    ocr->SetPageSegMode(tesseract::PSM_AUTO);
    ocr->SetImage(im.data, im.cols, im.rows, 3, im.step);
    
    outText = string(ocr->GetUTF8Text());
	ocr->End();
	
	return outText;
}
