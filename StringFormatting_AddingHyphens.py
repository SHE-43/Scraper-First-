# We are adding hyphens to words that may end up on two lines if the line limit has been achieved.

a = ("Enter your sentences here and do not type any line skipping commands, at all.");
print(a);

b = "Enter your sentences here and do not type any line skipping commands, at all. This sentence might go on for a very long time and might require the necessity and thus it should be made obsolete, totally obsolete."
c = "";
print(len(b));

print(b.rindex("here")) # this shows where the word index starts from.

reach = 0;
for word in b:
    the_length = len(b[0:reach]);
    reach += 1;
    if the_length >= 154:
        c = b[0:the_length] + "-" + "\n" + b[the_length:];
        break;

# Now, we need to start with the next line and count from the beginning of the line,
# We need to reset the counter and make sure that we deal with spaces, commas, apostrophe, Exclamation marks.
# In fact, all symbolic characters need another way of handling so that the editing goes exaclty 

print(c)




