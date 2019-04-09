def local(infine, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()
