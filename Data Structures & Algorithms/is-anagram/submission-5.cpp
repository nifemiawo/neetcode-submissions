class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sfreq;
        unordered_map<char,int> tfreq;

        for (char c : s){
            sfreq[c]+=1;
        }
        for (char c : t){
            tfreq[c]+=1;
        }

        if (sfreq == tfreq){
            return true;
        }

        return false;
    }
};
