edad = 20
#c#
#Console.WriteLine($"Tengo {edad} años\n");
#Console.WriteLine(@"Tengo {edad} años\n");

#python
print(f"Tengo {edad} años\n");
print(r"Tengo {edad} años\n");

a = "carlos 20 105148464 interbank"
b = "carlos|20|105148464|interbank"
print(a.split())
c=b.split("|")
print(c)
d="@".join(c)
print(d)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
z = spam.strip('Spam')
print(z)