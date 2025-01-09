const input = require('fs').readFileSync('input.txt', 'utf8').trim();
// const input = fs.readFileSync('/dev/stdin', 'utf8').trim();
// 'fs' 모듈을 사용하여 입력 데이터를 읽어옵니다.
// '/dev/stdin'에서 입력을 읽고, 문자열로 변환합니다.
// '/dev/stdin'은 온라인 저지 환경에서 표준 입력을 처리하는 데 사용됩니다.
// const input = require('fs').readFileSync('/dev/stdin').toString();

// DATType은 각 문자(q, u, a, c)의 카운트를 저장하기 위한 인터페이스를 정의합니다.
// 이 인터페이스는 각 키가 문자열이고 값은 숫자인 객체를 나타냅니다.
interface DATType {
  [key: string]: number;
}

// DAT 객체를 초기화하여 각 문자(q, u, a, c)의 카운트를 0으로 설정합니다.
// 각 문자의 카운트는 'quack' 문자열의 올바른 순서를 추적하는 데 사용됩니다.
const DAT: DATType = {
  q: 0, // 'q'의 카운트
  u: 0, // 'u'의 카운트
  a: 0, // 'a'의 카운트
  c: 0, // 'c'의 카운트
};

// splitWay는 동시에 발생할 수 있는 'quack'의 최대 개수를 추적합니다.
// 이는 각 문자의 총 카운트를 기반으로 계산됩니다.
let splitWay = 0;

// collectLetter 함수는 입력된 문자를 처리하고, DAT 객체를 업데이트합니다.
// 'quack' 문자열의 순서가 올바른지 확인하며, 순서가 잘못되었으면 -1을 출력하고 프로그램을 종료합니다.
function collectLetter(letter: string): void {
  if (letter === 'q') {
    // 'q'는 항상 새 'quack' 문자열의 시작입니다.
    // 'q'의 카운트를 증가시키고, splitWay를 현재 DAT 값들의 합계로 업데이트합니다.
    DAT['q'] += 1;
    splitWay = Math.max(splitWay, Object.values(DAT).reduce((a, b) => a + b, 0));
  } else if (letter === 'u') {
    // 'u'는 이전에 처리된 'q'가 있어야만 유효합니다.
    // 'q'의 카운트를 감소시키고, 'u'의 카운트를 증가시킵니다.
    if (DAT['q'] > 0) {
      DAT['q'] -= 1;
      DAT['u'] += 1;
    } else {
      // 'q'가 없으면 올바른 순서가 아니므로 -1을 출력하고 종료합니다.
      console.log(-1);
      process.exit(0);
    }
  } else if (letter === 'a') {
    // 'a'는 이전에 처리된 'u'가 있어야만 유효합니다.
    // 'u'의 카운트를 감소시키고, 'a'의 카운트를 증가시킵니다.
    if (DAT['u'] > 0) {
      DAT['u'] -= 1;
      DAT['a'] += 1;
    } else {
      console.log(-1);
      process.exit(0);
    }
  } else if (letter === 'c') {
    // 'c'는 이전에 처리된 'a'가 있어야만 유효합니다.
    // 'a'의 카운트를 감소시키고, 'c'의 카운트를 증가시킵니다.
    if (DAT['a'] > 0) {
      DAT['a'] -= 1;
      DAT['c'] += 1;
    } else {
      console.log(-1);
      process.exit(0);
    }
  } else if (letter === 'k') {
    // 'k'는 이전에 처리된 'c'가 있어야만 유효합니다.
    // 'c'의 카운트를 감소시킵니다. 'k'는 문자열이 끝남을 의미합니다.
    if (DAT['c'] > 0) {
      DAT['c'] -= 1;
    } else {
      console.log(-1);
      process.exit(0);
    }
  }
}

// 입력된 전체 문자열(rawText)을 순회하면서 각 문자를 처리합니다.
const rawText = input;

// 문자열의 각 문자를 반복하여 처리합니다.
for (const letter of rawText) {
  // 문자가 'quack'에 포함되어 있는 경우만 처리합니다.
  // 다른 문자는 무시합니다.
  if ('quack'.includes(letter)) {
    collectLetter(letter);
  }
}

// 반복이 끝난 후, 모든 DAT 값이 0이어야 합니다.
// DAT 값의 합계가 0이 아니면 'quack'이 올바르게 끝나지 않았음을 의미하므로 -1을 출력합니다.
if (Object.values(DAT).reduce((a, b) => a + b, 0) > 0) {
  console.log(-1);
  process.exit(0);
} else {
  // 모든 'quack' 문자열이 올바르게 처리되었으면 splitWay를 출력합니다.
  console.log(splitWay);
}
