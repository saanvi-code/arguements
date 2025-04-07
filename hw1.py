def shutdown(n):
    
    if n=="Yes" or "yes":
        print("shutting down")
    elif n=="No" or "no":
        print("aborting shut down")

    else:
        print("sorry")

shutdown("yes")
shutdown("no")
shutdown("Yes")
    