Tutorial git
============
- [Video git Collaboration, Sayanee Basu's](https://www.youtube.com/watch?time_continue=830&v=61WbzS9XMwk)
- [Tutorial from Sayanee Basu's](https://code.tutsplus.com/articles/team-collaboration-with-github--net-29876)
- [git Book](https://git-scm.com/book/en/v2)
- [github Help](https://help.github.com/categories/collaborating-with-issues-and-pull-requests)

Keterangan singkat
==================
- `git init` menciptakan direktori setting pada folder project
- `git clone` copy project dari repository
	- contoh untuk cloning project dengan url project `https://github.com/konpro-team/project`
	```
	git clone https://github.com/konpro-team/project
	```
- `git status` melihat status git dari project (penambahan file, perubahan kode, dll)
- `git add *nama file*` menambahkan file (file yang mengalami perubahan ataupun file baru) kedalam assigment untuk dilakukan commit
	- contoh untuk menambahkan file `README.md` yang sudah dirubah kodenya kedalam assigment 
	```
	git add README.md
	```
- `git remote add origin *url git*` menambahkan url git (repository) kedalam project
	- contoh untuk menambahkan url git kedalam project yang baru saja dibangun pada github. contoh url project pada github `git@github.com:konpro-team/project.git`
	```
	git remote add origin git@github.com:konpro-team/project.git
	```
- `git commit` mengijinkan assigment untuk bisa dilakukan push
	- contoh mengijinkan beberapa perubahan atau penambahan file yang telah dimasukan dalam assigment dengan pesan `file README.md sudah dirubah`
	```
	git commit -m "file README.md sudah dirubah"
	```
- `git push` melakukan perubahan terhadap kode atau file yang telah diberikan commit 
	- contoh melakukan push pada file yang sudah dilakukan commit
	```
	git push origin master
	```

Python Learners
===============
- [From Python Course](https://www.python-course.eu/python3_course.php)
- [Different of mutable and immutable object](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)