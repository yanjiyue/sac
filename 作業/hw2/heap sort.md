# 作業_Heap sort
## 1、流程圖
![Image text](https://github.com/yanjiyue/leecode/blob/master/heap1.png)
![Image text](https://github.com/yanjiyue/leecode/blob/master/heap2.png)
## 2、學習歷程
我參考了[https://baike.baidu.com/item/堆排序/2840151?fr=aladdin%EF%BC%89](https://baike.baidu.com/item/堆排序/2840151?fr=aladdin%EF%BC%89)其中關於堆的操作的說明，如下：
   ###
 `在堆的數據結構中，堆中的最大值總是位於根節點（在優先佇列中使用堆的話堆中的最小值位於根節點）。堆中定義以下幾種操作：`
* `最大堆調整（Max Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點`
* `創建最大堆（Build Max Heap）：將堆中的所有數據重新排序`
* `堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞歸運算`
與以下兩段代碼：
```C++
#include <iostream>
#include <algorithm>
using namespace std;
 
void max_heapify(int arr[], int start, int end) 
{
    //建立父節點指標和子節點指標
    int dad = start;
    int son = dad * 2 + 1;
    while (son <= end)  //若子節點指標在範圍內才做比較
    {    
        if (son + 1 <= end && arr[son] < arr[son + 1]) //先比較兩個子節點大小，選擇最大的
            son++;
        if (arr[dad] > arr[son]) //如果父節點大於子節點代表調整完畢，直接跳出函數
            return;
        else  //否則交換父子內容再繼續子節點和孫節點比較
        {
            swap(arr[dad], arr[son]);
            dad = son;
            son = dad * 2 + 1;
        }
    }
}
 
void heap_sort(int arr[], int len) 
{
    //初始化，i從最後一個父節點開始調整
    for (int i = len / 2 - 1; i >= 0; i--)
        max_heapify(arr, i, len - 1);
    //先將第一個元素和已經排好的元素前一位做交換，再從新調整(剛調整的元素之前的元素)，直到排序完畢
    for (int i = len - 1; i > 0; i--) 
    {
        swap(arr[0], arr[i]);
        max_heapify(arr, 0, i - 1);
    }
}
 
void main() 
{
    int arr[] = { 3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6 };
    int len = (int) sizeof(arr) / sizeof(*arr);
    heap_sort(arr, len);
    for (int i = 0; i < len; i++)
        cout << arr[i] << ' ';
    cout << endl;
    system("pause");
}
```
