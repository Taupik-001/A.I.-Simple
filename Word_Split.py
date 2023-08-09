import re
from docx import Document

# Sample text containing references
sample_text = [
    "B. Aboba, L. Blunk, J. Vollbrecht, J. Carlson, and H. Levkowetz, Extensible Authentication Protocol (EAP). Request for Comments: 3748, June 2004.",
    "Adi Shamir, Identity based cryptosystems and signatures, in Proceedings of Cryptology, Springer-Verlag, Berlin, 1984, pp. 47–53.BBBBB",
    "J.-L. Beuchat, E. Lpez-Trejo, L. Martnez-Ramos, S. Mitsunari, and F. Rodrguez-Henrquez, Multi-Core Implementation of the Tate Pairing Over Supersingular Elliptic Curves, Proceedings of the 8th International Conference in Cryptology and Network Security, 12– 14 December 2009.",
    "D. Boneh, and X. Boyen, Efficient selective-ID secure identity based encryption without random oracles, in Proc. of EUROCRYPT 04, LNCS, 3027, Springer Verlag, Interlaken, Switzerland, 2004, pp. 223–238.",
    "D. Boneh, and M. Franklin, Identity-based encryption from the weil pairing, in Proc. of CRYPTO 01, LNCS, 2139, Springer, Santa Barbara, CA, 2001, pp. 213–229.",
    "V. Cakulev, and I. Broustis, An EAP authentication method based on identity-based authenticated key exchange. draft-cakulev-emu-eap-ibake-03.txt, August 2012, work in progress 2012.",
    "V. Cakulev, G. Sundaram, and I. Broustis, IBAKE: identity-based authenticated key exchange, RFC 6539 2012. ISSN: 2070-1721.",
    "C. Ellison, and B. Schneier, Ten risks of PKI: what you’re not being told about public key infrastructure, Computer Security Journal 16(1) (2000), pp. 1–7.",
    "G. Frey, M. Muller, and H. Ru¨ck, The tate pairing and the discrete logarithm applied to elliptic curve cryptosystems, IEEE Transactions on Information Theory 45(5) (1999), pp. 1717–1719, 10.1109/18.771254.",
    "V. Kolesnikov, and G.S. Sundaram, IBAKE: Identity-Based Authenticated Key Exchange Protocol, The International Association for Cryptologic Research (IACR), Cryptology ePrint Archive 2011.",
    "Martijn Maas, Pairing-based cryptography. Master Thesis, Technische Universiteit Eindhoven 2004.",
    "C. Mulkey, D. Kar, and A. Katangur, Towards an Efficient Protocol for Privacy and Authentication in Wireless Networks, The 12th International Conference on Security and Management (SAM’13), July 2013.",
    "E. Rescorla, M. Ray, S. Dispensa, and N. Oskov, Transport Layer Security (TLS) Renegotiation Indication Extension, RFC 5746 2010.",
    "M.F. Sadikin, and M. Kyas, RFID-Tate: Efficient Security and Privacy Protection for Active RFID Over IEEE 802.15.4. The 5th International Conference on Information, Intelligence, Systems and Applications, IISA 2014.",
    "P. Szczechowiak, and M. Collier, Tinyibe: Identity-Based Encryption for Heterogeneous Sensor Networks, 5th International Conference on Intelligent Sensors, Sensor Networks, and Information Processing (ISSNIP), Melbourne, Australia, 2009, pp. 319–354.",
    "Vladimir Kolesnikov, and Charles Rackoff, Key exchange using passwords and long keys, in Theory of Cryptography, TCC, volume 3876 of LNCS, Springer, Columbia University, New York, NY, USA, 2006, pp. 100–119.",
    "Vladimir Kolesnikov, and Charles Rackoff, Password mistyping in two-factor- authenticated key exchange, in ICALP, Springer-Verlag, Reykjavik, Iceland, 2008, pp. 702–714.",
    "X. Xiong, D. Wong, and X. Deng, Tinypairing: A Fast and Lightweight Pairing-Based Cryptographic Library for Wireless Sensor Networks, IEEE Wireless Communications and Networking Conference (WCNC) 2010, pp. 1–6.",
]


def create_word_document(text, filename):
    # Create a new Word document and add the text to it
    doc = Document()
    doc.add_paragraph(text)
    
    # Save the document with the specified filename
    doc.save(filename)

# Generate separate Word documents for each entry in the sample_text list
for idx, text_entry in enumerate(sample_text, start=1):
    filename = f"{idx}.docx"
    create_word_document(text_entry, filename)
    print(f"Document {idx}:")
    print(text_entry)
    print("-" * 50)