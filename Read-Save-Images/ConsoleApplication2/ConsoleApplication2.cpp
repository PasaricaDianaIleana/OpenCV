#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main()
{

    vector<String> filenames;
  
    glob("D://pictures", filenames);

    for (int i = 0; i < filenames.size();i++)
    {
        Mat image = imread(filenames[i]);
    
   imwrite("D://saveFolder//" + to_string(i) +".jpg", image);
  

        if (!image.data)
            cerr << "No images" << endl;

     
    }
}

