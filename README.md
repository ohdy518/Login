# Login (w/ TinyDB, Salted Hash)

## 원리
  1. Signup.py에서 Password를 Salt와 Hash하고 Username, Email과 함께 TinyDB에 저장
  2. Login.py에서 Username의 존재 여부를 확인한 후 Password를 같은 방법으로 Hash하여 DB와 비교
  3. Hash 값이 같을 경우 액세스 허용, 다를 경우 액세스 거부

## 사용
  1. Signup.py로 가입
  2. Login.py로 로그인

## 라이선스 / License
**Login.py 및 Signup.py는 MIT License를 사용합니다. **


**Under MIT License. **
