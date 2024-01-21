import re


pattern = r".yclones"

text = '''The Indian subcontinent is one of the worst
          affected regions in the world. The subcontinent
          with a long coastline of 8041 kilometres is
          exposed to nearly 10 per cent of the world’s
          tropical cyclones. Of these, the majority of
          them have their initial genesis over the Bay of Bengal
          and strike the East coast of India. On an average,
          five to six tropical cyclones form every year,
          of which two or three could be severe. More
          cyclones occur in the Bay of Bengal than the
          Arabian Sea and the ratio is approximately 4:1.
          Cyclones occur frequently on both the coasts
          (the West coast - Arabian Sea; and the East coast - Bay of Bengal).
          An analysis of the frequency of cyclones on the
          East and West coasts of India between 1891 and 1990
          shows that nearly 262 cyclones occurred (92 of these severe)
          in a 50 km wide strip above the East coast.
          Less severe cyclonic activity has been noticed on
          the West coast, where 33 cyclones occurred the same
          period, out of which 19 of were severe. '''


matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    #print(match.span())
    #print(text[match.span()[0]: match.span()[1]])


# https://regexr.com/

#Find list of more meta characters here -
#https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

