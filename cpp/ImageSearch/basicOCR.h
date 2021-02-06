#ifndef BASIC_OCR_H
#define BASIC_OCR_H

#include <string>
#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>
#include <opencv2/opencv.hpp>

std::string getText(std::string imagePath);
 
#endif
