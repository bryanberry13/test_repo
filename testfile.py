print("this is my test file before I build my website")
echo "# test_repo" >> README.md
git init
git add testfile.py
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/bryanberry13/test_repo.git
git push -u origin main
