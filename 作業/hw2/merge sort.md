# Merge sort
## 1、流程圖
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/1.png)
## 2、學習歷程
參考了[https://baike.baidu.com/item/归并排序/1639015?fr=aladdin](https://baike.baidu.com/item/归并排序/1639015?fr=aladdin)中的歸併操作：
` 歸併操作(merge)，也叫歸併演算法，指的是將兩個順序序列合併成一個順序序列的方法。`
` 如　設有數列{6，202，100，301，38，8，1}`
`初始狀態：6,202,100,301,38,8,1`
`第一次歸併後：{6,202},{100,301},{8,38},{1}，比較次數：3；`
`第二次歸併後：{6,100,202,301}，{1,8,38}，比較次數：4；`
`第三次歸併後：{1,6,8,38,100,202,301},比較次數：4；`
`總的比較次數為：3+4+4=11；`
`逆序數為14；`
及演算法描述
`歸併操作的工作原理如下：`
`第一步：申請空間，使其大小為兩個已經排序序列之和，該空間用來存放合併後的序列`
`第二步：設定兩個指針，最初位置分別為兩個已經排序序列的起始位置`
`第三步：比較兩個指針所指向的元素，選擇相對小的元素放入到合併空間，並移動指針到下一位置`
`重複步驟3直到某一指針超出序列尾`
`將另一序列剩下的所有元素直接複製到合併序列尾`
及以下代碼：
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/1-2.png)
其中這段看不是很懂，但知道是用來切割的
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/1-3.png)
所以選擇了如下做法
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/2.png)
Def merge的部分本想如此做
#
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/3.png)
但出現如下錯誤：
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/4.png)
以及將原本的將小的數值逐個放入，改為將大的值逐個放入：
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/5.png)
但出現如下錯誤：
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/6.png)
## 3、文字說明
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/7.png)
merge sort之原理為先將數列切割為最小的list（長度為1）後比較組成長度為二倍的list，再將鄰組之間的數值分別比較插入；如此循環，直到list的長度變為原list的長度為止
![Image text](https://github.com/yanjiyue/leecode/blob/master/merge%20sort/8.png)
## 4、參考資料
[https://baike.baidu.com/item/归并排序/1639015?fr=aladdin](https://baike.baidu.com/item/归并排序/1639015?fr=aladdin)
