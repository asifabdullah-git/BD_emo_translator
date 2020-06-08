import codecs
encoding='utf-8'

__all__ = ['EMO_UNICODE', 'BD_UNICODE_EMO', 'EMOTICONS', 'EMOTICONS_EMO']

EMOTICONS = {
    u":‑\)": "হাসি মুখ",
    u":\)": "হাসি মুখ",
    u":-\]": "হাসি মুখ",
    u":\]": "হাসি মুখ",
    u":-3": "হাসি মুখ",
    u":3": "হাসি মুখ",
    u":->": "হাসি মুখ",
    u":>": "হাসি মুখ",
    u"8-\)": "ভালো লেগেছে",
    u":o\)": "ভালো লেগেছে",
    u":-\}": "ভালো লেগেছে",
    u":\}": "ভালো লেগেছে",
    u":-\)": "ভালো লেগেছে",
    u":‑D": "খুবই ভালো, আনন্দ",
    u":D": "খুবই ভালো, আনন্দ",
    u"8‑D": "খুবই ভালো, আনন্দ",
    u"8D": "খুবই ভালো, আনন্দ",
    u"X‑D": "খুব খুশি, আনন্দ",
    u"XD": "খুব খুশি, আনন্দ",
    u"=D": "মজা পেয়েছি",
    u"=3": "মজা পেয়েছি",
    u"B\^D": "মজা পেয়েছি",
    u":-\)\)": "খুব খুশি",
    u":‑\(": "খারাপ লেগেছে",
    u":-\(": "খারাপ লেগেছে",
    u":\(": "খারাপ লেগেছে",
    u":‑c": "খারাপ লেগেছে",
    u":c": "খারাপ লেগেছে",
    u":‑<": "খারাপ লেগেছে",
    u":'‑\(": "কান্না আসছে",
    u":'\(": "কান্না আসছে",
    u":'‑\)": "খুশি",
    u":'\)": "খুশি",
    u"D‑':": "ভয়",
    u"D:": "দুঃখ",
    u":‑O": "অবাক হয়েছি",
    u":O": "অবাক হয়েছি",
    u":‑o": "অবাক হয়েছি",
    u";‑\)": "চোখ মারা",
    u";\)": "চোখ মারা",
    u"\*-\)": "চোখ মারা",
    u":‑P": "ভেংচি",
    u":P": "ভেংচি",
    u"X‑P": "ভেংচি",
    u"XP": "ভেংচি",
    u":‑/": "লজ্জা, বিব্রত",
    u":/": "লজ্জা, বিব্রত",
    u":-[.]": "লজ্জা, বিব্রত",
    u">:[(\\\)]": "লজ্জা, বিব্রত",
    u">:/": "বিরক্ত, বিব্রত",
    u":[(\\\)]": "বিরক্ত, বিব্রত",
    u"=/": "বিরক্ত, বিব্রত",
    u"=[(\\\)]": "বিরক্ত, বিব্রত",
    u":‑x": "চুপ থাকা",
    u":x": "চুপ থাকা",
    u":‑#": "চুপ থাকা",
    u"O:‑\)": "পবিত্র, নিষ্পাপ",
    u"O:\)": "পবিত্র নিষ্পাপ",
    u"0:‑3": "পবিত্র, নিষ্পাপ",
    u"0:3": "পবিত্র, নিষ্পাপ",
    u"0;\^\)": "পবিত্র",
    u">:‑\)": "রাগান্বিত, খারাপ ,শয়তান ",
    u">:\)": "রাগান্বিত, খারাপ ,শয়তান",
    u"\}:‑\)": "রাগান্বিত, খারাপ ,শয়তান",
    u"\}:\)": "রাগান্বিত, খারাপ ,শয়তান",
    u"%‑\)": "মাতাল",
    u"%\)": "মাতাল",
    u":-###..": "অসুস্থ",
    u":###..": "অসুস্থ",
    u"\(-_-\)zzz": "ঘুম, ক্লান্ত",
    u"\(__\)": "সম্মানিত",
    u"_\(\._\.\)_": "সম্মানিত",
    u"<\(_ _\)>": "সম্মানিত",
    u"<m\(__\)m>": "ক্ষমা চাওয়া",
    u"m\(__\)m": "ক্ষমা চাওয়া",
    u"m\(_ _\)m": "ক্ষমা চাওয়া",
    u"\('_'\)": "কান্না, দুঃখ",
    u"\(/_;\)": "কান্না, দুঃখ",
    u"\(T_T\) \(;_;\)": "কান্না, দুঃখ",
    u"\(-\.-\)": "লজ্জা, খারাপ",
    u"\(-_-\)": "লজ্জা, খারাপ",
    u"\(一一\)": "লজ্জা, খারাপ",
    u":O o_O": "অবাক,চমকিত,উতলা",
    u"o_0": "অবাক,চমকিত,উতলা",
    u"o\.O": "অবাক,চমকিত,উতলা",
    u"\(\*￣m￣\)": "বিরক্ত, আহত, অসন্তুষ্ট",
    u':হাসি, ভালো :': u'U+1F600',

}

EMO_UNICODE = {
    u':হাসি, ভালো :': u'U+1F600',
    u':হাসি, ভালো:': u'\rU+1F603',
    u':রাগান্বিত,খারাপ,শয়তান:': u'\U0001F4A2',
    u':রাগান্বিত,খারাপ,শয়তান:': u'\U0001F620',
    u':রাগান্বিত,খারাপ,শয়তান:': u'\U0001F47F',
    u':অবাক,চমকিত,উতলা:': u'\U0001F632',
    u':ভালোবাসা:': u'\U0001F491',
    u':কান্না, দুঃখ:': u'\U0001F622',
    u':বিরক্ত, আহত, অসন্তুষ্ট:': u'\U0001F61E',
    u':ঘুম, ক্লান্ত:': u'\U0001F4AB',
    u':ঘুম, ক্লান্ত:': u'\U0001F635',
    u':ভালোবাসা, চুম্বন:': u'\U0001F618',
    u':ভয়, চিৎকার:': u'\U0001F631',
    u':চুম্বন:': u'\U0001F48F',
    u':কান্না,চিৎকার:': u'\U0001F62D',
    u':মিথ্যাবাদী:': u'\U0001F925',
    u':অশ্লীল,খারাপ:': u'\U0001F595',
    u':বিষন্ন,চিন্তিত:': u'\U0001F614',
    u':প্রশ্নবোধক,জিজ্ঞাসা:': u'\U00002753',
    u':ঘুম,বিরক্ত:': u'\U0001F62A',
    u':হাসি, ভালো :': u'\U0000263A',
    u':হাসি, ভালো ,:': u'\U0001F607',
    u':হাসি, ভালো ,:': u'\U0001F600',
    u':বোকা হাসি,বিব্রত:': u'\U0001F60F',
    u':চিন্তিত,উদ্বিগ্ন,অশান্ত,উদ্বেগপূর্ণ,ঝামেলাপূর্ণ:': u'\U0001F914',
    u':বিজয় চিহ্ন:': u'\U0000270C',
    u':ক্লান্ত,পরিশ্রান্ত,অবসন্ন,গ্লান:': u'\U0001F629',
    u':নারী, মহিলা, স্ত্রী:': u'\U0001F469',
    u':চিন্তিত,উদ্বিগ্ন:': u'\U0001F61F',
    u':হাসি,আনন্দ, খুশি, উল্লাস:': u'\U0001F606',
    u':হাসি,আনন্দ, খুশি, উল্লাস:': u'1F600',
    u"1F600": "হাসি,আনন্দ, খুশি, উল্লাস",



}

BD_UNICODE_EMO = {v: k for k, v in EMO_UNICODE.items()}

EMOTICONS_EMO = {

   # u"😀": "হাসি,আনন্দ, খুশি, উল্লাস",
   # u':হাসি, ভালো :': u'U+1F600',
    u"1F600": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":‑)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":-]": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":]": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":-3": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":3": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":->": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":>": "হাসি,আনন্দ, খুশি, উল্লাস",
    u"8-)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":o)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":-}": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":}": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":-)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":c)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":^)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u"=]": "হাসি,আনন্দ, খুশি, উল্লাস",
    u"=)": "হাসি,আনন্দ, খুশি, উল্লাস",
    u":‑D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u":D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"8‑D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"8D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"X‑D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"XD": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"=D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"=3": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u"B^D": "অট্টহাস্য, অট্টহাস, অট্টহাসি,উল্লাস",
    u":-))": "আনন্দ, খুশি",
    u":-(": "রাগান্বিত,খারাপ,শয়তান",
    u":‑(": "রাগান্বিত,খারাপ,শয়তান",
    u":(": "রাগান্বিত,খারাপ,শয়তান",
    u":‑c": "রাগান্বিত,খারাপ,শয়তান",
    u":c": "রাগান্বিত,খারাপ,শয়তান",
    u":‑<": "রাগান্বিত,খারাপ,শয়তান",
    u":<": "রাগান্বিত,খারাপ,শয়তান",
    u":‑[": "রাগান্বিত,খারাপ,শয়তান",
    u":[": "রাগান্বিত,খারাপ,শয়তান",
    u":-||": "রাগান্বিত,খারাপ,শয়তান",
    u">:[": "রাগান্বিত,খারাপ,শয়তান",
    u":{": "রাগান্বিত,খারাপ,শয়তান",
    u":@": "রাগান্বিত,খারাপ,শয়তান",
    u">:(": "রাগান্বিত,খারাপ,শয়তান",
    u":'‑(": "কান্না, দুঃখ",
    u":'(": "কান্না, দুঃখ",
    u"D‑':": "ভয়, আশঙ্কা, ভীতি, শঙ্কা",
    u"D:<": "বিতৃষ্ণা, অসাধ, বিরাগ, ঘৃণা",
    u"D:": "কান্না, দুঃখ",
    u":‑O": "অবাক,চমকিত,উতলা",
    u":O": "অবাক,চমকিত,উতলা",
    u":‑o": "অবাক,চমকিত,উতলা",
    u":o": "অবাক,চমকিত,উতলা",
    u":-0": "ধাক্কা,আঘাত,ঘুষি",
    u"8‑0": "ক্লান্ত,জড়তা",
    u">:O": "ক্লান্ত,জড়তা",
    u":-*": "ভালোবাসা, চুম্বন",
    u":*": "ভালোবাসা, চুম্বন",
    u":X": "ভালোবাসা, চুম্বন",
    u";‑)": "ইশারা,মজা, তামাশা",
    u";)": "ইশারা,মজা, তামাশা",
    u"*-)": "ইশারা,মজা, তামাশা",
    u"*)": "ইশারা,মজা, তামাশা",
    u";‑]": "ইশারা,মজা, তামাশা",
    u";]": "ইশারা,মজা, তামাশা",
    u";^)": "ইশারা,মজা, তামাশা",
    u":‑,": "ইশারা,মজা, তামাশা",
    u";D": "ইশারা,মজা, তামাশা",
    u":‑/": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":/": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":-[.]": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u">:[(\)]": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u">:/": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":[(\)]": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u"=/": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u"=[(\)]": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":L": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u"=L": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":S": "অস্থির,অসুবিধা,বিক্ষুব্ধ,উত্তেজিত",
    u":$": "লজ্জা, বিব্রত",
    u"O:)": "পবিত্র নিষ্পাপ",
    u"0:‑3": "পবিত্র নিষ্পাপ",
    u"0:3": "পবিত্র নিষ্পাপ",
    u"0:‑)": "পবিত্র নিষ্পাপ",
    u"0:)": "পবিত্র নিষ্পাপ",
    u"0;^)": "পবিত্র নিষ্পাপ",
    u">:‑)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u">:)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u"}:‑)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u"}:)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u"3:‑)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u"3:)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u">;)": "রাগ,ঘৃণা,শয়তান,খারাপ",
    u"|‑O": "উদাস,একঘেয়েমি",
    u"%‑)": "মাতাল",
    u"%)": "মাতাল",
    u":-###..": "অসুস্থ",
    u":###..": "অসুস্থ",
    u"(^^>``": "বিভ্রান্ত, অপ্রস্তুত, হতবুদ্ধি,লজ্জা,বিনয়",
    u"(^_^;)": "বিভ্রান্ত, অপ্রস্তুত, হতবুদ্ধি,লজ্জা,বিনয়",
    u"(-_-;)": "বিভ্রান্ত, অপ্রস্তুত, হতবুদ্ধি,লজ্জা,বিনয়",
    u"(~_~;) (・.・;)": "বিভ্রান্ত, অপ্রস্তুত, হতবুদ্ধি,লজ্জা,বিনয়",
    u"(-_-)zzz": "ঘুম, ক্লান্ত",
    u"((+_+))": "অপ্রস্তুত, হতবুদ্ধি,লজ্জা",
    u"(+o+)": "অপ্রস্তুত, হতবুদ্ধি,লজ্জা",
    u"^_^": "আনন্দ, খুশি",
    u"(^_^)/": "আনন্দ, খুশি",
    u"(^O^)／": "আনন্দ, খুশি",
    u"(^o^)／": "আনন্দ, খুশি",
    u"(__)": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"_(._.)_": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"<(_ _)>": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"<m(__)m>": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"m(__)m": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"m(_ _)m": "সম্মান, মান্য, সম্ভ্রম, শ্রদ্ধা, সুনাম, আদর",
    u"('_')": "কান্না, দুঃখ",
    u"(/_;)": "কান্না, দুঃখ",
    u"(T_T) (;_;)": "কান্না, দুঃখ",
    u"(;_:)": "কান্না, দুঃখ",
    u"(;O;)": "কান্না, দুঃখ",
    u"(:_;)": "কান্না, দুঃখ",
    u"(ToT)": "কান্না, দুঃখ",
    u";_;": "কান্না, দুঃখ",
    u";-;": "কান্না, দুঃখ",
    u";n;": "কান্না, দুঃখ",
    u";;": "কান্না, দুঃখ",
    u"Q.Q": "কান্না, দুঃখ",
    u"T.T": "কান্না, দুঃখ",
    u"QQ": "কান্না, দুঃখ",
    u"Q_Q": "কান্না, দুঃখ",
    u"(-.-)": "লজ্জা, অপমান, শরম, গ্লানি, কলঙ্ক",
    u"(-_-)": "লজ্জা, অপমান, শরম, গ্লানি, কলঙ্ক",
    u"(一一)": "লজ্জা, অপমান, শরম, গ্লানি, কলঙ্ক",
    u"(；一_一)": "লজ্জা, অপমান, শরম, গ্লানি, কলঙ্ক",
    u"(=_=)": "ক্লান্তি, অবসাদ",
    u">^_^<": "হাসি,ভালো",
    u"<^!^>": "হাসি,ভালো",
    u"^/^": "হাসি,ভালো",
    u"（*^_^*）": "হাসি,ভালো",
    u"(^<^) (^.^)": "হাসি,ভালো",
    u"(^^)": "হাসি,ভালো",
    u"(^.^)": "হাসি,ভালো",
    u"(^_^.)": "হাসি,ভালো",
    u"(^_^)": "হাসি,ভালো",
    u"(^^)": "হাসি,ভালো",
    u"(^J^)": "হাসি,ভালো",
    u"(*^.^*)": "হাসি,ভালো",
    u"(^—^）": "হাসি,ভালো",
    u"(#^.^#)": "হাসি,ভালো",
    u"(*^0^*)": "উত্তেজিত, বিক্ষুব্ধ",
    u"(*_*)": "বিস্মিত, অবাক্",
    u"(*_*;": "বিস্মিত, অবাক্",
    u"(+_+) (@_@)": "বিস্মিত, অবাক্",
    u'(-"-)': "বিক্ষুব্ধ,রাগী",
    u"(ーー;)": "ক্ষুব্ধ,রাগী",
    u":O o_O": "অবাক,চমকিত,উতলা",
    u"o_0": "অবাক,চমকিত,উতলা",
    u"o.O": "Surpised",
    u"(o.o)": "অবাক,চমকিত,উতলা",
    u"oO": "অবাক,চমকিত,উতলা",
    u"(*￣m￣)": "বিরক্ত, আহত, অসন্তুষ্ট",

}