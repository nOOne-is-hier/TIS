#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
using namespace std;

// 유효성 검증 함수
bool is_valid(const unordered_map<char, int>& count_letters, const unordered_map<char, int>& required_count) {
    for (const auto& key : { 'A', 'C', 'G', 'T' }) {
        if (count_letters.at(key) < required_count.at(key)) {
            return false;
        }
    }
    return true;
}

int main() {
    ifstream input("input.txt"); // input.txt 파일에서 입력 읽기
    if (!input) {
        cerr << "파일을 열 수 없습니다." << endl;
        return 1;
    }

    // 입력 초기화
    int S, P;
    input >> S >> P;

    string raw_text;
    input >> raw_text;

    int A, C, G, T;
    input >> A >> C >> G >> T;

    unordered_map<char, int> required_count = { {'A', A}, {'C', C}, {'G', G}, {'T', T} };
    unordered_map<char, int> count_letters = { {'A', 0}, {'C', 0}, {'G', 0}, {'T', 0} };

    int promise_case = 0;

    // 슬라이딩 윈도우 초기화
    for (int i = 0; i < P; ++i) {
        count_letters[raw_text[i]]++;
    }

    // 초기 윈도우 유효성 검사
    if (is_valid(count_letters, required_count)) {
        promise_case++;
    }

    // 슬라이딩 윈도우 실행
    for (int i = P; i < S; ++i) {
        // 왼쪽 문자 제거
        count_letters[raw_text[i - P]]--;
        // 오른쪽 문자 추가
        count_letters[raw_text[i]]++;

        // 현재 윈도우 유효성 검사
        if (is_valid(count_letters, required_count)) {
            promise_case++;
        }
    }

    // 결과 출력
    cout << promise_case << endl;

    return 0;
}
