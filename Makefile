system-up:
	docker run -d -p 80:80 tmc-system

system-ini:
	make system-install
	make system-up

system-reset:
	make system-down
	make system-up

system-down:
	docker rm -f tmc-system

system-install:
	docker build -t tmc-system .
