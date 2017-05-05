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
int showreadvideo() {
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
		cvtColor(frame, edges, CV_BGR2GRAY);
		Canny(edges, edges, 0, 30, 3);
		// edges = frame;

		imshow("edges", edges);

		// make delay
		waitKey(100);
		// wait for 30 seconds
		// if (waitKey(30000) >= 0) {
		// 	break;
		// }
	}
	// it will free source automatically by cap after quit
	return 0;
}

// write video
int showwritevideo() {
	Size s(320, 240);

	VideoWriter writer = VideoWriter("output/myvideo0.avi", CV_FOURCC('M', 'J', 'P', 'G'), 25, s);

	if (!writer.isOpened()) {
		cerr << "cannot create video file." << endl;
		return -1;
	}

	Mat frame(s, CV_8UC3);

	for (int i = 0; i < 100; ++i) {
		frame = Scalar::all(255);
		char text[128];

		snprintf(text, sizeof(text), "%dth", i);

		putText(frame, text, Point(s.width/3, s.height/3), FONT_HERSHEY_SCRIPT_SIMPLEX, 3, Scalar(0, 255, 255), 3, 8);
		// write the image into video
		writer << frame;
	}
	return 0;
}

// my display
int test() {
	// Mat image(600, 800, CV_8UC3);
	// Mat image = imread("WindowsLogo.jpg");

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

	// if (image.empty()) {
	// 	cout << "cannot load iage." << endl;
	// 	return -1;
	// }

	// Mat result;
	// Canny(image, result, 50, 150);

	// write it into windowslogl-canny.png
	// imwrite("WindowsLogo-canny.png", result);

	// imshow("image", image);
	// imshow("result", result);

	Size s(640, 480);
	VideoWriter writer = VideoWriter("output/myvideo1.avi", CV_FOURCC('M', 'J', 'P', 'G'), 2, s);

	for (int i = 1; i <= 14; ++i) {
		string imagename;

		stringstream stream;
		stream << "data/left" << i << ".jpg";

		stream >> imagename;

		Mat frame = imread(imagename);

		if (frame.empty()) {
			cout << "cannot load image." << endl;
			break;
		}

		writer << frame;
	}

	// waitKey(0);

	return 0;
}

int main(int argc, char **argv) {
	// showat();
	// showiterator();
	// showreadvideo();
	// showwritevideo();

	test();
} 