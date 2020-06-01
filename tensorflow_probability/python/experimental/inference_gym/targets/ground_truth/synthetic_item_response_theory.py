# Lint as: python2, python3
# Copyright 2020 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
r"""Ground truth values for `synthetic_item_response_theory`.

Automatically generated using the command:

```
bazel run //tools/inference_gym_ground_truth:get_ground_truth -- \
  --target \
  synthetic_item_response_theory \
  --stan_samples \
  50000 \
```
"""

import numpy as onp

IDENTITY_MEAN_STUDENT_ABILITY_MEAN = onp.array([
    0.07407780940224962,
]).reshape(())

IDENTITY_MEAN_STUDENT_ABILITY_MEAN_STANDARD_ERROR = onp.array([
    0.0008707657869347018,
]).reshape(())

IDENTITY_MEAN_STUDENT_ABILITY_STANDARD_DEVIATION = onp.array([
    0.11197835313284824,
]).reshape(())

IDENTITY_QUESTION_DIFFICULTY_MEAN = onp.array([
    -1.7386134475919999,
    0.4970258902902354,
    1.4344515468160002,
    1.641429930172,
    -1.001773881264,
    0.2327278244741427,
    1.1243957450820001,
    -0.07559818087100739,
    -1.4440410689700003,
    1.5331072539439998,
    1.0109075684440003,
    1.0993926030260002,
    1.0008861356779999,
    -0.5607651194998506,
    -1.839558199016,
    0.6157032862357659,
    0.28316118897229803,
    -1.3930272628359999,
    -0.1826951549828188,
    -0.27245178856736113,
    -1.3238985986440002,
    -0.7889031974784,
    -0.629952581408262,
    0.90073743814,
    -0.634451995103406,
    1.07784211796,
    0.39487005242700796,
    0.7102433332581601,
    -0.22943065911830432,
    2.1791148153,
    0.3098560530447122,
    -0.4780290339603407,
    0.4171185387587336,
    -0.929333270144,
    0.01294210999174574,
    -0.16320760854581498,
    -0.72957786402666,
    -0.008774799387835337,
    0.2759720422917563,
    0.627329170600476,
    -0.607592383396456,
    -1.049087797634,
    -0.236599294154692,
    -0.024498208985064728,
    1.291555356934,
    -0.06889535398832192,
    1.3722089347600002,
    0.3805027608634775,
    -0.0976881344257036,
    0.965523356652,
    1.183840026494,
    -1.6039984834439998,
    0.5329468077083179,
    -0.5170399530101487,
    -0.3217317937651375,
    -0.8679235757419999,
    0.7910547048319361,
    0.5155459551574353,
    0.932831712898,
    -0.30386777959856576,
    0.65220167045662,
    0.23627015969942233,
    -0.8982357515989999,
    0.40516740677637825,
    0.1100365360794964,
    -1.2240389583979998,
    -0.14391360383527788,
    -0.931383929464,
    -1.3094086595539998,
    0.08232204964352068,
    0.28010321076742106,
    -0.21117574411016715,
    -0.3036128893657573,
    1.381981250282,
    0.5698702942150142,
    -1.1702289528979999,
    -2.0633761805999997,
    -1.258155670806,
    -0.10903028372803954,
    -0.5808749584725981,
    1.6144416303100002,
    0.3801686252274436,
    1.229021142386,
    0.7957122265339999,
    0.8231759003185999,
    0.862264107036,
    -1.480945797932,
    -0.05874234330316512,
    -0.04207072342839674,
    -1.4291671972400002,
    -0.24515205664346684,
    0.2174140920427668,
    -2.30767872408,
    -0.254459719645339,
    -1.342952374268,
    -0.39624365341949636,
    -0.07064649124210468,
    1.4426443779959999,
    -0.7329086047286,
    2.8889239935599997,
]).reshape((100,))

IDENTITY_QUESTION_DIFFICULTY_MEAN_STANDARD_ERROR = onp.array([
    0.0008302688548113903,
    0.0008377517344524241,
    0.0008321175849093665,
    0.0008347728688133536,
    0.0008281721337753032,
    0.0008379325213730962,
    0.0008292481395888176,
    0.0008347895922602316,
    0.0008279643036566825,
    0.0008434549165918242,
    0.0008318796317302861,
    0.0008335214577500402,
    0.0008298823723502089,
    0.0008307300086792171,
    0.0008312541076548566,
    0.0008386895707374964,
    0.0008364389939085418,
    0.0008363893404864511,
    0.0008317526678195214,
    0.000833399635423499,
    0.0008399245591492785,
    0.0008244676504408693,
    0.0008452481044063678,
    0.0008357020080111191,
    0.0008365818821648423,
    0.000836739112200339,
    0.0008325497987036042,
    0.0008325827491677793,
    0.0008304742207482917,
    0.0008353939843338689,
    0.0008327627836690308,
    0.0008395559653867722,
    0.00083471930030518,
    0.0008306375242686843,
    0.0008346349200822218,
    0.0008379523345081949,
    0.0008343677087542545,
    0.0008263287958796913,
    0.0008306656100065513,
    0.0008329747087928184,
    0.0008386372261955543,
    0.000833040050935524,
    0.0008357591099290488,
    0.0008278722812990439,
    0.0008317177959206316,
    0.0008322555719500899,
    0.0008284495734618935,
    0.0008307460415443434,
    0.00083431329264272,
    0.0008318617754617958,
    0.0008341511735774881,
    0.0008318694755599152,
    0.0008297461193562304,
    0.0008319329352222202,
    0.0008343048075938506,
    0.0008372311587521407,
    0.0008381539319232146,
    0.0008308702096690273,
    0.0008344629089750782,
    0.0008289645967878066,
    0.0008242539285040097,
    0.000833993393978764,
    0.0008364670310790112,
    0.0008305226650771719,
    0.0008356646160099807,
    0.0008392421387432828,
    0.0008264871417932329,
    0.000827252487053729,
    0.0008303942298105111,
    0.0008304800196125167,
    0.0008301383282270659,
    0.0008359593595189047,
    0.0008322258600597539,
    0.0008270496330697541,
    0.0008334836475599582,
    0.0008352430204730789,
    0.0008314542128219164,
    0.0008365574367892898,
    0.0008365269330817332,
    0.000832120732131346,
    0.0008425776087297702,
    0.0008466629270993518,
    0.0008318047534406957,
    0.0008369411157594329,
    0.000832539591661743,
    0.000842619013391847,
    0.0008350133163141549,
    0.0008250079348652423,
    0.0008290982368429107,
    0.0008316588928771712,
    0.0008267783479902109,
    0.0008307608606418441,
    0.0008412217881701981,
    0.0008366204539802397,
    0.0008335447678819271,
    0.0008411102156922019,
    0.000834263313320927,
    0.0008255609425307198,
    0.0008292887956098761,
    0.0008342698890570286,
]).reshape((100,))

IDENTITY_QUESTION_DIFFICULTY_STANDARD_DEVIATION = onp.array([
    0.19017135448372158,
    0.162819951082574,
    0.17402545582900222,
    0.1820817104371582,
    0.17366555964694247,
    0.1571395384782796,
    0.16772167706384994,
    0.16136687759851204,
    0.18010916364899882,
    0.17838892755633004,
    0.16686427951436475,
    0.16796625276407362,
    0.16815499080699614,
    0.16361926806791727,
    0.19334303017815638,
    0.16009115090484416,
    0.15952084094147587,
    0.1760441353594948,
    0.15994730382234315,
    0.1621617301282396,
    0.17296681112317416,
    0.16525565942598144,
    0.1648193502075456,
    0.1648551685980192,
    0.16593273911684836,
    0.1679321535199737,
    0.15942540730027077,
    0.16212928413872107,
    0.16430309343396984,
    0.19871247126425526,
    0.16125748282508606,
    0.16311682757398924,
    0.16480311538358602,
    0.16688833742969125,
    0.1615286497952559,
    0.16179329412597496,
    0.16562234292717024,
    0.15912745401827486,
    0.16098194022840587,
    0.16366689611446134,
    0.16316840530746693,
    0.1704103020358691,
    0.16397021517071111,
    0.1586622047109239,
    0.1735483326629893,
    0.160958350599367,
    0.17763375253878508,
    0.15998639694393943,
    0.1633977627750487,
    0.16459602822272784,
    0.16669677298727512,
    0.1843541999111087,
    0.16320312725822309,
    0.16322279440335835,
    0.16124012910420343,
    0.1666897685147499,
    0.1609479273337171,
    0.1616371666386907,
    0.16616042903371395,
    0.1619882063583902,
    0.16423776637599816,
    0.16195949947738947,
    0.16718000871582586,
    0.1630887022032364,
    0.1599585331515819,
    0.17402542003665328,
    0.160134484479293,
    0.16623035308753262,
    0.17762185774875405,
    0.16281794094912955,
    0.16138382477254196,
    0.16312302474809293,
    0.16122549070334602,
    0.16985285764238753,
    0.1628811634633817,
    0.17436778068388226,
    0.19976911365410505,
    0.17212764494973917,
    0.15726283514804865,
    0.1639711864113929,
    0.18100393485540206,
    0.16197457263789833,
    0.1733668443106707,
    0.16349179347804524,
    0.16423000212969757,
    0.16434776401329063,
    0.18065316238254644,
    0.16177087036034404,
    0.1599154184055926,
    0.17696293715489916,
    0.16177582267446725,
    0.16119554373748715,
    0.20628526679004286,
    0.16105394199241257,
    0.1745881166840509,
    0.16174697192838156,
    0.159861503742484,
    0.17633579241510886,
    0.16560336771279552,
    0.23592272716407298,
]).reshape((100,))

IDENTITY_STUDENT_ABILITY_MEAN = onp.array([
    -1.53145329601,
    -0.1037224805984333,
    -2.5346325862340002,
    -0.16659334202409193,
    0.6892170580765797,
    -1.6299039882208,
    0.5759216326428854,
    -0.6154707631470533,
    -1.324495666496,
    0.26573155400430587,
    0.7652577314690523,
    0.45544409607823655,
    0.5238103874501941,
    -0.07197163890352715,
    -0.4030064082278912,
    -0.06367757260774272,
    1.683101206428,
    0.22385358625675966,
    -1.1513866702117999,
    0.548573036566933,
    0.95948719891944,
    0.09658737436078371,
    -0.25508354878122896,
    0.3639320319599111,
    0.13172360741438932,
    1.0503049746552402,
    -0.45477945750018983,
    -1.2402264559735998,
    0.024592244501932516,
    -0.1869129383995491,
    -0.20193764465813402,
    0.7348782572302233,
    0.3891360234108299,
    -0.8764053289629732,
    0.6220997721656951,
    -0.5073001317697317,
    0.5771299509476774,
    -0.3244893565756618,
    -0.5967372128658794,
    0.8906601567501482,
    0.5054662723805192,
    -0.8233170183430492,
    -0.94152715900854,
    0.055102367547591215,
    0.2875787010788121,
    -0.11052142642368387,
    -2.45172990148,
    0.4821019754025249,
    0.27328559476535663,
    0.6733012052892752,
    -0.5971436128798498,
    -0.32638502085487964,
    1.20211811798238,
    0.007431183893937379,
    -0.1617339404895533,
    -0.5249321455865328,
    -0.2957169904034686,
    -0.18469260962941791,
    0.18060040981340936,
    0.35473971988064823,
    -0.6641263517903532,
    0.2525559187533776,
    -0.7539204182644546,
    -0.3329978298430479,
    -0.23733742775601177,
    -0.760337975514854,
    -1.4409460175180002,
    -1.8339906816679998,
    0.30437866433659694,
    0.40769991369333053,
    -0.2635777799139569,
    -0.024379979858648763,
    1.191782711065,
    1.8064755678079998,
    0.08579855190709651,
    -0.3495977374279837,
    0.5307887255771849,
    -0.32494071333992347,
    0.9759680251663667,
    -1.708893196914,
    1.19285887578,
    1.464530109598,
    -0.047362513238781816,
    -0.7175787668705759,
    -0.3554173763286351,
    0.7810222199058319,
    0.0445688914121763,
    -0.7058807897119578,
    -1.4744592470979998,
    0.96031031521877,
    0.15924372958751498,
    -0.4557929645883889,
    1.49168204254,
    -0.5948206225035152,
    0.991245166309044,
    -0.2852341028182611,
    0.4404589654398972,
    0.15386423849687042,
    -0.72617522138649,
    -1.20941258117032,
    0.22926366029767,
    0.5272633759166432,
    0.1501467809611307,
    -1.16153582106686,
    1.5419183981584,
    -1.3076265565060001,
    -0.4238912646086758,
    -0.014768106259741082,
    -2.5742700496879993,
    1.2329021759498002,
    -0.3422795359497348,
    1.1682863691695182,
    -1.029187952559037,
    -0.11244665804012433,
    -1.6738904437400002,
    -1.1391955747795999,
    -1.0902649463342,
    0.996376733766717,
    -0.0036802422203173974,
    0.8527621863064899,
    -0.21480769984946807,
    1.4014786028615398,
    0.3742453176585132,
    0.16925068096584048,
    1.4265286825399999,
    1.1742408021920803,
    1.8449258754400002,
    0.7205603994245529,
    -0.23815166731438545,
    -1.7780341281040002,
    0.1620075008428395,
    0.7325721512168284,
    1.5654199944240001,
    0.26359842124964705,
    -0.46459631768461057,
    -1.511834487334,
    -0.1625684778689565,
    -0.367417644599748,
    0.6468749458098315,
    0.1373447899928501,
    0.9399144748567302,
    0.6760378888460012,
    0.11272579724195722,
    0.8259415655944972,
    -0.26474734528528693,
    0.45917341156354796,
    -1.459245022712,
    -1.02317726654718,
    1.978101300314,
    -1.9986051595099998,
    -1.68247514906,
    0.5779341614433877,
    -1.372992027352,
    -0.32739473994169555,
    -1.5945308304920003,
    -1.0624877080104003,
    0.9614425731603798,
    0.6047045076063853,
    -1.68376286521,
    0.5589677921527343,
    0.6137186195302284,
    0.18753607337665934,
    0.9890195621768738,
    0.8095195434092533,
    -0.3965986380923612,
    1.377445820116,
    -0.06838985422610416,
    2.046548337596,
    0.9164617542965511,
    -0.3195634095572081,
    1.0314516889874399,
    0.7108559007045535,
    1.862238528658,
    1.3621603174541999,
    -0.8267514363812998,
    -0.02198228824454651,
    0.7617448542479179,
    0.44623613896832126,
    -0.4158880793516606,
    2.4915407061940003,
    0.5118227624437395,
    0.16764792450445937,
    -1.097660859342,
    -0.48194520472199337,
    -1.2524319852227999,
    -1.3287868312196,
    -0.934167280992282,
    -0.006831081480208742,
    -0.03926775662275091,
    -1.35273229923,
    1.547476519466,
    1.9184099788800002,
    0.4773887663715793,
    -1.02138403404478,
    0.8504069605922153,
    -1.737402300094,
    -1.681245128506,
    -1.004367689798912,
    0.6467059961667293,
    0.29001215231698685,
    0.3648311896598303,
    -0.26138861419812937,
    -2.279267307414,
    -0.0906688334915982,
    -2.031979872194,
    -2.3078282275440003,
    -1.2519677743818,
    0.7470155445163321,
    -0.5818845335287651,
    0.08863238859381536,
    0.96987595096648,
    -0.7213854069945482,
    -0.2012063756434957,
    -1.2219291561363002,
    -1.5417369252720001,
    -0.545967865179587,
    0.8798168529091672,
    -1.7416170762179999,
    -1.2491089371948,
    1.426395042546,
    1.784180046686,
    -0.18744309517350596,
    1.2823936394620001,
    -0.5633369317002368,
    2.1333581553420005,
    -0.04484150799137086,
    1.35685118387,
    1.439285213142,
    0.8845448792462859,
    0.6252844100642271,
    0.909542824717998,
    0.5839097948280497,
    -1.7248625863540004,
    0.21788342843553538,
    -0.6435830284776212,
    1.3210799375539999,
    0.1415838021001044,
    1.8362484038000002,
    -0.2019487394330007,
    -1.6032595213639997,
    -1.0205622517486,
    0.08421743324607722,
    -0.5810183405009883,
    1.0852629189064,
    -0.7776757258059481,
    0.21938508585720937,
    -1.2181636793408,
    0.8204301774150642,
    -1.522501076094,
    1.4530306969039999,
    2.235335521786,
    0.5477739229160095,
    0.35840048782709544,
    1.0167107552091,
    -1.1864072267484,
    -0.12236532921975521,
    0.1337068970997462,
    0.2141363627733126,
    -0.22390538554576436,
    0.93889574165009,
    -0.05000929121623153,
    1.7368487523799998,
    -1.07996802297094,
    -1.28701371198194,
    0.5689810048889178,
    -0.6128465630766041,
    0.3370081809060027,
    -0.4519495649238655,
    -0.37731409274448513,
    0.8724509235420881,
    0.5619742599209652,
    0.6004137651405483,
    -0.576758348260154,
    -0.8571399339024343,
    -0.25358060126713355,
    -0.011058305219536048,
    0.050647048616681165,
    -1.3917808357538,
    1.45607680543,
    -0.0879312861849905,
    -1.654818923574,
    1.555989578466,
    2.287911787794,
    0.049078671349419956,
    1.10820104755586,
    -1.0565198412581478,
    -0.48633814120482877,
    -0.096486118539407,
    0.840825936870066,
    0.409057122325647,
    -0.09663701001849348,
    -0.22716427462073688,
    -0.9052941303019708,
    -0.48155094190290687,
    0.10716636791521161,
    -0.9191790975503323,
    -0.5462467839702463,
    1.5756277384039998,
    1.589474114636,
    1.0643347737643203,
    -1.7413775472159998,
    -0.029742328333474354,
    -1.082055631271144,
    -1.003215040359684,
    -0.24980362354872584,
    -0.24579682722733484,
    0.6441752072047096,
    1.5448193510200003,
    0.4303396845693279,
    -0.9798921964558998,
    0.09703427879389323,
    -0.9501522859627786,
    -0.22866924287891927,
    -0.8176927980886936,
    -0.020132374965521324,
    0.25133523889129894,
    -0.30283341985744244,
    1.1134931961458803,
    -0.6693667692775632,
    0.47177153321636406,
    -0.17964803201251905,
    -0.6202410169739533,
    -0.12483988879780886,
    1.1535818084061,
    0.2437626226045569,
    0.05486687186624295,
    0.2576491588469953,
    -1.5055650762579995,
    0.3306273076220177,
    -1.2455774615348,
    -0.2363778988814813,
    1.278181048935852,
    2.0080525314939996,
    -0.9766116511207219,
    0.046840084894934284,
    0.0059391695437916595,
    -0.6038452662638061,
    -2.400121061816,
    -0.9982711311217599,
    1.9224614175519998,
    -1.142826721446204,
    -0.12573405741197605,
    -0.947665710873094,
    0.6661696920140205,
    0.4715697391822512,
    -0.8385178105043781,
    -0.007437700784033481,
    -1.1493230316026,
    -0.5275137858395749,
    1.3799628333996,
    0.5954848667305329,
    -0.22227881062663765,
    -0.31437605125491186,
    0.5469087128027968,
    0.6068641291515311,
    0.2855400400124261,
    -0.8716571643172324,
    -0.07494768277257863,
    0.4160823900674475,
    -0.09069102924585433,
    0.16808100918351976,
    1.1672069613254001,
    0.4087921158301694,
    0.35216162425810726,
    0.3641058507879814,
    -0.6930345286539217,
    0.660464211651983,
    0.4886364312786261,
    0.2282901088633266,
    0.2901760382059634,
    0.4111575398698338,
    0.3289383994245535,
    0.7085954448202112,
    0.958119369306554,
    -1.1877120774862,
    0.5490385521521295,
    1.679664647616,
    0.5038420360679283,
    -1.1671936104944003,
    0.027194053939753444,
    -0.2589797922975594,
    0.38039782810007666,
    0.14086498991109658,
    0.37141237054180143,
    1.1277811727083802,
    0.1070007410622342,
    -1.2661088301419998,
    1.559182573428,
    1.4419045370119998,
    0.5013072236186092,
    -1.537873881282,
    -1.2839242075015997,
    -0.29227794986234923,
    -1.399358003376,
    -0.4731158765279423,
    -0.3554884864521684,
    -0.7558993274806871,
    -0.6073432014296761,
    0.39718177205072713,
    0.4216300384822055,
]).reshape((400,))

IDENTITY_STUDENT_ABILITY_MEAN_STANDARD_ERROR = onp.array([
    0.0003807302090591504,
    0.0003522319768193471,
    0.0004612581242175986,
    0.00037233459890380496,
    0.00036813477007659065,
    0.00040346353947745594,
    0.00037716760132062565,
    0.00036440615018271604,
    0.00038338353360423095,
    0.00035551931808240096,
    0.0003878285060591543,
    0.00036553540889735944,
    0.0003672849144539399,
    0.0003559158675279467,
    0.00036774637765694685,
    0.00035584316175129406,
    0.0004100652510117891,
    0.0003614737870315838,
    0.0003763080829250638,
    0.00036258399122052497,
    0.00037062337188633026,
    0.00035952242226359614,
    0.00034949770550229606,
    0.00036135250077889904,
    0.0003507853040426144,
    0.0003739014924998915,
    0.00035925606627960937,
    0.0003918742701085739,
    0.00036488097277403373,
    0.0003539950197775601,
    0.00035788937003609407,
    0.0003810531574596075,
    0.0003530930989026296,
    0.000373652718691511,
    0.000383935808921923,
    0.00035974094297714005,
    0.00035945313729555576,
    0.000356307484630763,
    0.0003600378876822727,
    0.0003719156257651956,
    0.00037539407688620056,
    0.0003598352772400606,
    0.0003675260846244555,
    0.00037320139465658896,
    0.00037363121862067964,
    0.00035568866619706724,
    0.000455593887580432,
    0.00037463987029125173,
    0.0003529895206765149,
    0.00036433494782583915,
    0.00036675435173932913,
    0.0003642664467200116,
    0.00038735721352350444,
    0.000370165099303707,
    0.00035481420011045827,
    0.0003666255174125307,
    0.00036725408498696865,
    0.0003668077438855692,
    0.00035567673907868766,
    0.000358763844540175,
    0.000369377234552482,
    0.00036942748008708535,
    0.0003617971386527043,
    0.00035199369056704017,
    0.0003600321834619692,
    0.0003641632702028392,
    0.00038046767184268533,
    0.00040095450783722965,
    0.000369067240014855,
    0.00036255496810369184,
    0.00036965259314812864,
    0.0003582663673375366,
    0.00037383361304930767,
    0.0004087152848087334,
    0.0003614546506474394,
    0.0003540879274365029,
    0.0003610307423805708,
    0.00036035278020724786,
    0.00036896278024262644,
    0.0004135925755213107,
    0.0003723170552022848,
    0.000381127959602535,
    0.00035709960118430513,
    0.00036550104612138016,
    0.00036400837309123486,
    0.0003682639794316729,
    0.00035697903982153577,
    0.0003725223269775804,
    0.0003913300917201865,
    0.0003849373110788112,
    0.0003597848118033653,
    0.00037200795208787305,
    0.00039898713244806066,
    0.0003672184918186208,
    0.00036814988237644336,
    0.00035101942382774584,
    0.0003679460362332782,
    0.0003526543221436749,
    0.0003678829050565934,
    0.00038747124574698094,
    0.00035415662376175265,
    0.0003762103071361496,
    0.00035819290608919674,
    0.00038700899517328573,
    0.0004016959254991072,
    0.00037461980749164936,
    0.0003678306991589346,
    0.00035138047158923347,
    0.0004567454202688617,
    0.0003799345604212541,
    0.00036245215041054375,
    0.000386248142688457,
    0.0003688397776543128,
    0.00036352189158027923,
    0.00040052048371455904,
    0.00037953770231504834,
    0.0003805847868712634,
    0.0003653802170589804,
    0.000364608962886792,
    0.00037826215143391644,
    0.0003651780171923358,
    0.0004012466537631555,
    0.0003765363298664247,
    0.00036275617949365377,
    0.000380564531763498,
    0.0003793092227224019,
    0.0004240988403902765,
    0.0003617351088771606,
    0.0003666715898575965,
    0.0004052767112719767,
    0.00036621383398398875,
    0.0003696887506493269,
    0.0003984845256617444,
    0.0003677710693980309,
    0.0003621443520454881,
    0.0003950132149528491,
    0.0003432926613372743,
    0.0003641850557654326,
    0.0003676036258547077,
    0.0003588796772385077,
    0.0003682293331372077,
    0.0003660702457507916,
    0.00035516638627752,
    0.000370852192373612,
    0.00035310276189749284,
    0.0003714396274595556,
    0.0003790063312430169,
    0.0003759663040796095,
    0.00040772126780319785,
    0.00040366879952233314,
    0.00039506613767557056,
    0.00036291280849009834,
    0.00037525308260390856,
    0.00036414631519378685,
    0.0003955039932472967,
    0.00037762600352939335,
    0.0003699447965960905,
    0.00037461162440837815,
    0.0004075696833431024,
    0.0003689658866572577,
    0.00034949146586574063,
    0.00035882019341426066,
    0.00037662952086823685,
    0.0003719831645069374,
    0.00036382089718362833,
    0.00038929620653461246,
    0.00035387697589122524,
    0.0004381846293264442,
    0.0003664333752466361,
    0.00036054828637699274,
    0.000371383877655576,
    0.0003709123062027061,
    0.0004168290118117364,
    0.00039517545692547564,
    0.00037226316697589753,
    0.00037034688815825925,
    0.0003697448537950147,
    0.0003609366563049233,
    0.00036345888618116647,
    0.00046859265761287647,
    0.00035721704117589565,
    0.0003663697501293001,
    0.00037782899071418173,
    0.00035671820586256057,
    0.0003891940868550363,
    0.00037878718171461965,
    0.00038371942337721564,
    0.0003580556436759882,
    0.0003630539024365288,
    0.0003854670288165862,
    0.0003914478014214124,
    0.0004163329814745157,
    0.00036460977031165957,
    0.0003687311306047335,
    0.00038518911923230337,
    0.000412893566103962,
    0.00039652549633799436,
    0.00038794730288420456,
    0.0003704237010648445,
    0.00036799602571981364,
    0.0003604353639146432,
    0.00036547742928468545,
    0.0004555573092694083,
    0.00035075158947902555,
    0.0004208422868677193,
    0.00043741350915649674,
    0.00037435552675476333,
    0.0003636880184436686,
    0.0003562922353409024,
    0.0003719484411337716,
    0.0003728730973876976,
    0.0003741061821975788,
    0.000365773818221504,
    0.00038179893805347645,
    0.0003805261674614682,
    0.00036699822153150587,
    0.0003698498905112882,
    0.0003903428900367587,
    0.00037725081915066346,
    0.0004044262640293855,
    0.00041860787526739517,
    0.0003577066501726797,
    0.00037892621734971133,
    0.000362959011114616,
    0.00045002118491843505,
    0.00036380851700783663,
    0.0003773511300547562,
    0.0003917472586305837,
    0.00036277610092309246,
    0.00038314393650407336,
    0.0003688956843713889,
    0.00036309555337999256,
    0.0004265472404619288,
    0.00035703504744172,
    0.00036221099190272013,
    0.0003820099813639321,
    0.00036334876423314085,
    0.00042931278296406896,
    0.000364806758778768,
    0.0003770688886557176,
    0.00036730304437165926,
    0.00035816051675740537,
    0.0003541142792497701,
    0.0003881009361259791,
    0.0003725741170525413,
    0.0003718129053264026,
    0.000370270557700957,
    0.0003758347558785034,
    0.0003961814955513416,
    0.000385312488406763,
    0.0004392452018197106,
    0.00036869036616538926,
    0.000374666153433015,
    0.00036288941115501946,
    0.00037584714700667534,
    0.0003640704737019748,
    0.0003644895411918226,
    0.0003538984814201486,
    0.00036472011466662517,
    0.0003689003788535386,
    0.0003691853799068832,
    0.000416380299337264,
    0.00036190811348160023,
    0.0003753197361449902,
    0.0003672347995766353,
    0.0003675511098308543,
    0.00035352129408548885,
    0.0003585069108085392,
    0.00036599380952045913,
    0.00036350510576376344,
    0.000371432758361592,
    0.00036866506480644266,
    0.00037053853107533996,
    0.0003572077295874529,
    0.0003683914801964893,
    0.0003648159405076817,
    0.0003562655047625727,
    0.000403375322273615,
    0.00039949338681271235,
    0.000379102265376018,
    0.000409931871492805,
    0.0003932527531735471,
    0.000436597784539377,
    0.0003600490616658104,
    0.0003891875674337495,
    0.00036957226478249154,
    0.00035342782946904154,
    0.0003626533840942856,
    0.0003702441341222138,
    0.0003643505758639582,
    0.0003536051714895676,
    0.000377525436297279,
    0.0003830511209776495,
    0.0003596789889391157,
    0.00036379582672639246,
    0.0003715530663200229,
    0.00037315439798680746,
    0.0004017409398717018,
    0.0004109307223246848,
    0.0003820512689593424,
    0.0003973311157613765,
    0.0003569094217948375,
    0.00037551505993846536,
    0.0003701537878040545,
    0.00036072686122383516,
    0.0003523569290086269,
    0.00036750463325126013,
    0.0003949306587657855,
    0.00037003876828469655,
    0.0003682657333053287,
    0.00036072069153839537,
    0.0003783540918314163,
    0.0003652452639984381,
    0.00036910287850852667,
    0.0003617361977340996,
    0.000371069664140319,
    0.0003636867776412704,
    0.0003733552646810362,
    0.0003642719885312381,
    0.00036295018275303527,
    0.0003606321467873895,
    0.00037426628888793744,
    0.00037300664834235284,
    0.0003784877139382366,
    0.00035635643204248285,
    0.0003635298932313777,
    0.00037387964614753134,
    0.0003848988576014691,
    0.00037040846085119734,
    0.000377322149229602,
    0.0003726480391635172,
    0.00038244295350270304,
    0.0004255783290901482,
    0.00037102506740369746,
    0.00036130410686998867,
    0.00034978139532361495,
    0.00037029564103098977,
    0.00042911874148569666,
    0.00037604008635943334,
    0.0004454009481920099,
    0.0003901307038984549,
    0.0003757699834126286,
    0.000370912844545672,
    0.00037032189045495696,
    0.00036605897754326216,
    0.00036012527650128014,
    0.00036192401388643563,
    0.000363925013289729,
    0.000364603469657287,
    0.00039076439653393914,
    0.00036094082283042,
    0.00035873139418905465,
    0.00036627932170654363,
    0.0003750214573050499,
    0.00036434729367850003,
    0.00035878891413729876,
    0.000374899005486041,
    0.0003665897964713611,
    0.00035388747073936556,
    0.0003575134823336028,
    0.000359987621262818,
    0.0003776514377249224,
    0.00036239457382840335,
    0.00036508855372201405,
    0.00035228063202594965,
    0.00037474523932526366,
    0.00035892474517833266,
    0.0003660691816453079,
    0.00036579093656706306,
    0.0003696000194876975,
    0.0003657733844544186,
    0.00036072720584771613,
    0.00037543824926729915,
    0.00036176653791076,
    0.00038761400074055437,
    0.0003649893982094239,
    0.00038546866508923095,
    0.00036532735340006104,
    0.00035523125391524686,
    0.00036757872019585306,
    0.0003591065221869966,
    0.00035769186496412706,
    0.00036089089661395295,
    0.00037555550743583155,
    0.0003824322930941847,
    0.00035958346298408116,
    0.0003707048052761983,
    0.00040627179899909913,
    0.0004005050949485239,
    0.000374085983650575,
    0.00038223179110346916,
    0.00038092474173882253,
    0.00035763246212672597,
    0.0003771685540587141,
    0.0003624347182018015,
    0.0003603300710283619,
    0.00036041302648390065,
    0.0003718109978406836,
    0.00037141759129414963,
    0.00036169298560581126,
]).reshape((400,))

IDENTITY_STUDENT_ABILITY_STANDARD_DEVIATION = onp.array([
    0.2791090859688944,
    0.24336611422837376,
    0.36488692494203334,
    0.26018895473099024,
    0.2511594289001522,
    0.2986992866573224,
    0.25762706405510805,
    0.2570941822037678,
    0.28273088076979863,
    0.25691498392195766,
    0.2695415193098069,
    0.26260821352992314,
    0.2604856275626116,
    0.24721600067764782,
    0.2610540342671481,
    0.24720639782118434,
    0.30855546810084217,
    0.25856536828353893,
    0.2758506049677941,
    0.25574614430139153,
    0.2708123083380415,
    0.24500437243787507,
    0.24135314849422698,
    0.2560154401471106,
    0.24132530628703272,
    0.2695215283822754,
    0.24872132141141604,
    0.28540385895697995,
    0.25121663717159554,
    0.24315075978233,
    0.24993846595083263,
    0.27188832402009727,
    0.23610580622883276,
    0.2748067175419838,
    0.2794311787777723,
    0.2525963319198097,
    0.24498433483221435,
    0.2550849692565974,
    0.25056828587590957,
    0.2730984535597845,
    0.2525550378893956,
    0.25705979784826855,
    0.25336774670357964,
    0.2625639509250063,
    0.2615016961696125,
    0.2478446098247033,
    0.3706619032362402,
    0.2721104219396517,
    0.2547605741351998,
    0.25744218189656326,
    0.2535551772648442,
    0.255151893725088,
    0.28326556513292955,
    0.2570822971742373,
    0.24469798086476863,
    0.25185648939454486,
    0.24558990083321083,
    0.26324598590824116,
    0.25293007894185804,
    0.2439706424342551,
    0.268124375948917,
    0.2552230492834867,
    0.2577849693131578,
    0.24563382105052134,
    0.26077683404238794,
    0.2675695661856813,
    0.27765626662304654,
    0.3040410369250185,
    0.25804948426308677,
    0.2491917842488701,
    0.2454533427973807,
    0.24634281409225173,
    0.2725895760070548,
    0.31487922691516385,
    0.24717719451828865,
    0.24078790971335592,
    0.24438981907803076,
    0.2534966611673324,
    0.2662138910649684,
    0.3056252061333474,
    0.26715718769129265,
    0.2741468282110619,
    0.2526001189473998,
    0.2633496782137194,
    0.2545974734718209,
    0.26723717309701345,
    0.24399931887365622,
    0.25696373939435296,
    0.28618043109070734,
    0.27926978390379015,
    0.2515093817147499,
    0.25826754093078336,
    0.3008294466251549,
    0.2512858187655407,
    0.2687126304923245,
    0.24095702987274095,
    0.25881204528138174,
    0.24070902223659446,
    0.25852272504393314,
    0.2781185408770773,
    0.24799855391507072,
    0.26581376077742214,
    0.24628475111659723,
    0.2810258704677224,
    0.30141788587509755,
    0.27488261879896536,
    0.2554797610258617,
    0.24724239271687729,
    0.3653993104787058,
    0.28313807441613215,
    0.24631215611434137,
    0.2855485842686902,
    0.2620100011768667,
    0.25069081956572015,
    0.298899897642608,
    0.2754209546257453,
    0.27109833160368835,
    0.26293191110933,
    0.25202914312623703,
    0.2739028748721043,
    0.2564665943891778,
    0.305086977681739,
    0.25884774164269786,
    0.2582601530908254,
    0.2799436296926646,
    0.27497089417026327,
    0.33025678971602535,
    0.2550035051722592,
    0.2563868018180513,
    0.30410687146615123,
    0.256154575553928,
    0.26712953038055465,
    0.2984487116991167,
    0.25745216414985556,
    0.2610758337740001,
    0.29939234482885696,
    0.24101448794144797,
    0.25035831861484253,
    0.2645405993048917,
    0.25099771928256265,
    0.26663483147590933,
    0.26519591337455206,
    0.2509018861298411,
    0.2741645501661662,
    0.23909640522841008,
    0.2650778697941769,
    0.27156648081833945,
    0.27237682823419307,
    0.3137881383151027,
    0.3063628120099805,
    0.2914831884100581,
    0.25223772913353476,
    0.2735979015246753,
    0.2580483556449678,
    0.2987255590983629,
    0.28126878008555734,
    0.2649849782034522,
    0.26538866638713493,
    0.3076189078674919,
    0.26538170177042175,
    0.24289705790737148,
    0.25300916927231654,
    0.2706830440046038,
    0.26416941760162177,
    0.2510320672357696,
    0.27998417088863464,
    0.24166184753502926,
    0.3472118868257862,
    0.26256072596398783,
    0.24897199442935883,
    0.27418886360985234,
    0.27091568262890026,
    0.32045013392765165,
    0.282568610532477,
    0.2597404735808616,
    0.257989842363703,
    0.2681895254569828,
    0.2625635437839696,
    0.26055110922162733,
    0.383911029207819,
    0.26050244444017084,
    0.2570758800753336,
    0.26984726430607187,
    0.25340432729271867,
    0.28656054354632904,
    0.2690441819506373,
    0.2737299430614805,
    0.2513214610100176,
    0.2533661129830128,
    0.2828849149080148,
    0.2915563039217558,
    0.3205484300367759,
    0.2512688007881092,
    0.26294404787989717,
    0.26892740261652537,
    0.32287700571997097,
    0.29165485945053377,
    0.27361430788308216,
    0.2532239373678148,
    0.2630272919883222,
    0.25752669177127135,
    0.2561164144476695,
    0.3557402358006939,
    0.24408331910983216,
    0.325702771429707,
    0.3427785403967338,
    0.2727648898741722,
    0.25962426154561036,
    0.2500984680653627,
    0.2618965985022919,
    0.26479723913685904,
    0.2681486456822141,
    0.24872645468050741,
    0.2758038957731256,
    0.28856832250567843,
    0.2673669580224761,
    0.25510514852447147,
    0.2918063322397543,
    0.27023096787145817,
    0.29657132145663023,
    0.3212807517200081,
    0.2493591205917213,
    0.2739309182704085,
    0.25266005392607205,
    0.3487501679388922,
    0.2530649492022645,
    0.27646954058407697,
    0.28596744434967053,
    0.25866921851209124,
    0.2773964446508175,
    0.2697509713809395,
    0.2647393536163582,
    0.3220689838490454,
    0.25036331807135603,
    0.2626897216133877,
    0.27864522371495615,
    0.25629503857968466,
    0.33234784562285385,
    0.2602837553873588,
    0.28233041034198236,
    0.2708837068348031,
    0.25089398525771955,
    0.24591899289512612,
    0.2937185434300251,
    0.2673630861190074,
    0.2607150390963616,
    0.2682987961935724,
    0.26534550596617346,
    0.2905842246100582,
    0.283167959537041,
    0.3423514636691657,
    0.27125697418902456,
    0.26207846631569626,
    0.2679342602933034,
    0.2728067553498931,
    0.24930845660634882,
    0.2629162752425466,
    0.24261711388578666,
    0.2565257584469081,
    0.2650410869025861,
    0.25197080340934186,
    0.31075255559930637,
    0.25854116404301597,
    0.2736684502877284,
    0.2620243832090361,
    0.2613185406380435,
    0.2552143432033847,
    0.2433824816143216,
    0.2538261414397999,
    0.25982557184073396,
    0.2632873040084761,
    0.2667663027932888,
    0.2609566047817372,
    0.25940820099040574,
    0.25707444776657595,
    0.2565239065210773,
    0.24523338738109116,
    0.2994858773613719,
    0.2948700075095576,
    0.27082530936180527,
    0.30627066796015356,
    0.2931662517611125,
    0.3545184965520302,
    0.24866625666453118,
    0.27861071935216986,
    0.2639965032512805,
    0.24459360345125383,
    0.26183654205577805,
    0.2675007295508,
    0.25335054538511365,
    0.25528097101686537,
    0.26484700344330964,
    0.28138650919044633,
    0.2498944329341119,
    0.2604563875916717,
    0.26166882295507404,
    0.2608050264872015,
    0.2998548539301914,
    0.3075410373041991,
    0.28122010210308857,
    0.29700323571126364,
    0.25857892600817073,
    0.27693549200200995,
    0.2614167920718378,
    0.25227843203123085,
    0.2450179702732253,
    0.26729321673951995,
    0.2975012692503899,
    0.2613424411686331,
    0.2673662572079564,
    0.2574412888082601,
    0.2742384855106804,
    0.2547892897433899,
    0.2708322212449492,
    0.2556519665561132,
    0.2625410816300757,
    0.26972310164382823,
    0.2698529278785143,
    0.2569436227082871,
    0.2529405660275751,
    0.25397117342987763,
    0.26872874728630036,
    0.2677297908348233,
    0.27378847375549,
    0.2456498721226803,
    0.2578097780284807,
    0.2583542154415034,
    0.2919876422728699,
    0.26217618142653837,
    0.274337128803326,
    0.2582892645892646,
    0.2732577979943262,
    0.3374419829795458,
    0.26357909089067666,
    0.24926309807113575,
    0.24219165523765046,
    0.25702593802716,
    0.3382896728648203,
    0.2720436608257121,
    0.35302987925578344,
    0.28662665818642685,
    0.264700483789464,
    0.2619217992190076,
    0.26537366001751816,
    0.2546191007394235,
    0.2571973682122088,
    0.24790933645942959,
    0.2612423406707779,
    0.25260614575056983,
    0.29937532659953925,
    0.250236033168029,
    0.25093676665287334,
    0.2520000659806788,
    0.2584095733583529,
    0.26174686311024714,
    0.25257421403730895,
    0.2618658313213285,
    0.2591516195561422,
    0.2463739702873769,
    0.2546007777593006,
    0.2550097758403467,
    0.27689494135681864,
    0.2543644941373353,
    0.25890700383357645,
    0.24656132398443947,
    0.26504416301906913,
    0.25973220772639954,
    0.2571657464776395,
    0.25249577369984494,
    0.2582673768170921,
    0.2525367220756647,
    0.24756331138521995,
    0.27397364914823213,
    0.26531392689606953,
    0.2777931390263465,
    0.25719766678363903,
    0.2983622368770872,
    0.2558656717901,
    0.2536996834148389,
    0.2520603133326972,
    0.2516849070915258,
    0.2601904867135497,
    0.2556761106007976,
    0.26262709131134687,
    0.28331062764652437,
    0.2581051312929231,
    0.2671924923775289,
    0.3060407132458062,
    0.2998580192800292,
    0.2757486432174753,
    0.27936044376100627,
    0.2789154591086189,
    0.24838324677018875,
    0.2765160229171123,
    0.24841840617501038,
    0.2539376325457054,
    0.25798554006782065,
    0.257360396807066,
    0.26017033675196327,
    0.2508344710663564,
]).reshape((400,))
