// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        int vectSize = pairs.size();
        vector<vector<Pair>> res;

        for (int unsortedPointer = 0; unsortedPointer < vectSize; ++unsortedPointer) {
            int sortedPointer = unsortedPointer - 1;

            while (sortedPointer >= 0 && (pairs[sortedPointer].key > pairs[sortedPointer + 1].key)) {
                swap(pairs[sortedPointer], pairs[sortedPointer + 1]);
                --sortedPointer;
            }

            res.push_back(pairs);
        }

        return res;
    }
};
