import server
import sys

if __name__ == "__main__":
	try:
		server.Server().serve()
	except KeyboardInterrupt as msg:
		sys.exit(0)