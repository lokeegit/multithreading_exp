# multithreading_exp

Code 1: Multithreading in Merge Sort and Performance Comparison
This program sorts a list of numbers using the merge sort algorithm with multithreading. Normally, merge sort splits the list into two halves, sorts them individually, and merges them back together. In this version, instead of sorting the left and right halves one by one, two separate threads are used so both halves get sorted at the same time. After both threads complete their tasks, the code merges the sorted halves. This approach can help improve performance, especially for large lists, because the sorting work is divided and done simultaneously.

Code 2: Multithreading in Quick Sort and Performance Comparison
This code sorts a large list of random numbers using quicksort in two different ways—one using the regular method (single-threaded) and the other using multithreading. In the single-threaded version, the list is sorted recursively in the usual way. In the multithreaded version, two threads are used to sort the left and right sides of the list after choosing a pivot. The program records the time taken by both methods and prints the results. This lets you see how using threads can improve the speed of quicksort when dealing with large amounts of data.

Code 3: Downloading Multiple Files Using Multithreading
This program downloads three images from the internet and compares the speed between normal downloading and multithreaded downloading. In the first part, the images are downloaded one after another using a simple loop. In the second part, each image download runs in its own thread, so all images are downloaded at the same time. The program measures the time taken in both cases and prints it out. Since multithreading allows the downloads to happen in parallel, it usually finishes faster than the one-by-one method.

