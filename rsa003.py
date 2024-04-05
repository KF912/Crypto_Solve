import gmpy2
import binascii

e = 65537
p = 104046835712664064779194734974271185635538927889880611929931939711001301561682270177931622974642789920918902563361293345434055764293612446888383912807143394009019803471816448923969637980671221111117965227402429634935481868701166522350570364727873283332371986860194245739423508566783663380619142431820861051179
q = 140171048074107988605773731671018901813928130582422889797732071529733091703843710859282267763783461738242958098610949120354497987945911021170842457552182880133642711307227072133812253341129830416158450499258216967879857581565380890788395068130033931180395926482431150295880926480086317733457392573931410220501
c = 4772758911204771028049020670778336799568778930072841084057809867608022732611295305096052430641881550781141776498904005589873830973301898523644744951545345404578466176725030290421649344936952480254902939417215148205735730754808467351639943474816280980230447097444682489223054499524197909719857300597157406075069204315022703894466226179507627070835428226086509767746759353822302809385047763292891543697277097068406512924796409393289982738071019047393972959228919115821862868057003145401072581115989680686073663259771587445250687060240991265143919857962047718344017741878925867800431556311785625469001771370852474292194

phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
m = gmpy2.powmod(c,d,p*q)
print(hex(m)[2:])
print(binascii.unhexlify(hex(m)[2:]))

