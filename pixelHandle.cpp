#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;

// use at function
int showat() {
	Mat grayim(600, 800, CV_8UC1);
	Mat colorim(600, 800, CV_8UC3);

	for (int i = 0; i < grayim.rows; ++i) {
		uchar *p = grayim.ptr<uchar>(i);
		for (int j = 0; j < grayim.cols; ++j) {
			// grayim.at<uchar>(i, j) = (i + j) % 255;
			p[j] = (i + j) % 255;
		}
	}

	for (int i = 0; i < colorim.rows; ++i) {
		Vec3b *p = colorim.ptr<Vec3b>(i);
		for (int j = 0; j < colorim.cols; ++j) {
			// Vec3b pixel;
			// pixel[0] = i % 255;
			// pixel[1] = j % 255;
			// pixel[2] = 0;
			// colorim.at<Vec3b>(i, j) = pixel;
			p[j][0] = i % 255; // blue
			p[j][1] = j % 255; // green
			p[j][2] = 0;	   // red
		}
	}
	imshow("grayim", grayim);
	imshow("colorim", colorim);

	waitKey(0);

	return 0;
}

// use iterator
int showiterator() {
	Mat grayim(600, 800, CV_8UC1);
	Mat colorim(600, 800, CV_8UC3);

	MatIterator_<uchar> grayit, grayend;

	for (grayit = grayim.begin<uchar>(), grayend = grayim.end<uchar>(); grayit != grayend; ++grayit) {
		*grayit = rand() % 255;
	}
	MatIterator_<Vec3b> colorit, colorend;
	for (colorit = colorim.begin<Vec3b>(), colorend = colorim.end<Vec3b>(); colorit != colorend; ++ colorit) {
		(*colorit)[0] = rand() % 255; //blue
		(*colorit)[1] = rand() % 255; //green
		(*colorit)[2] = rand() % 255; //red
	}

	imshow("grayim", grayim);
	imshow("colorim", colorim);

	waitKey(0);
	return 0;
}

// read video
int showvideo() {
	VideoCapture cap("vtest.avi");

	if (!cap.isOpened()) {
		cerr << "cannot open a camera or file." << endl;
		return -1;
	}

	Mat edges;

	namedWindow("edges", 1);

	while (true) {
		Mat frame;
		cap >> frame;

		if (frame.empty()) {
			break;
		}
		// cvtColor(frame, edges, CV_BGR2GRAY);
		// Canny(edges, edges, 0, 30, 3);
		edges = frame;

		imshow("edges", edges);

		// wait for 30 seconds
		if (waitKey(30) > 0) {
			break;
		}
	}
	// it will free source automatically by cap after quit
	return 0;
}

// my display
int test() {
	// Mat image(600, 800, CV_8UC3);
	Mat image = imread("WindowsLogo.jpg");

	// for (int i = 0; i < image.rows; ++i) {
	// 	Vec3b *pixel = image.ptr<Vec3b>(i);
	// 	for (int j = 0; j < image.cols; ++j) {
	// 		// Vec3b pixel;
	// 		// pixel[0] = (i + j) % 255;
	// 		// pixel[1] = 0;
	// 		// pixel[2] = 0;
	// 		pixel[j][0] = 0;
	// 		pixel[j][1] = 0;
	// 		pixel[j][2] = 0;
	// 	}
	// }

	// for (int i = 0; i < image.rows; ++i) {
	// 	Vec3b *pixel = image.ptr<Vec3b>(i);
	// 	for (int j = 0; j < image.cols; ++j) {
	// 		double gray = (pixel[j][0] + pixel[j][1] + pixel[j][2]) / 3;
	// 		pixel[j][0] = pixel[j][1] = pixel[j][2] = gray;
	// 	}
	// }

	if (image.empty()) {
		cout << "cannot load iage." << endl;
		return -1;
	}

	Mat result;
	Canny(image, result, 50, 150);

	// write it into windowslogl-canny.png
	imwrite("WindowsLogo-canny.png", result);

	// imshow("image", image);
	imshow("result", result);

	waitKey(0);
	return 0;
}

int main(int argc, char **argv) {
	// showat();
	// showiterator();
	showvideo();

	// test();
} 