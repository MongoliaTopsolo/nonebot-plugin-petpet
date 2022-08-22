from .utils import Meme
from .functions import *

memes = [
    Meme("universal", universal, ("万能表情", "空白表情")),
    Meme("petpet", petpet, ("摸", "摸摸", "摸头", "rua"), r"摸摸?头?|rua"),
    Meme("kiss", kiss, ("亲", "亲亲"), r"亲亲?"),
    Meme("rub", rub, ("贴", "贴贴", "蹭", "蹭蹭"), r"贴贴?|蹭蹭?"),
    Meme("play", play, ("顶", "玩")),
    Meme("pat", pat, ("拍",)),
    Meme("rip", rip, ("撕",)),
    Meme("throw", throw, ("丢", "扔")),
    Meme("throw_gif", throw_gif, ("抛", "掷")),
    Meme("crawl", crawl, ("爬",)),
    Meme("support", support, ("精神支柱",)),
    Meme("always", always, ("一直",)),
    Meme("loading", loading, ("加载中",)),
    Meme("turn", turn, ("转",)),
    Meme("littleangel", littleangel, ("小天使",)),
    Meme("dont_touch", dont_touch, ("不要靠近",)),
    Meme("alike", alike, ("一样",)),
    Meme("roll", roll, ("滚",)),
    Meme("play_game", play_game, ("玩游戏",), r"来?玩游戏"),
    Meme("worship", worship, ("膜", "膜拜"), r"膜拜?"),
    Meme("eat", eat, ("吃",)),
    Meme("bite", bite, ("啃",)),
    Meme("police", police, ("出警",)),
    Meme("police1", police1, ("警察",)),
    Meme("ask", ask, ("问问",), r"去?问问"),
    Meme("prpr", prpr, ("舔", "舔屏", "prpr"), r"舔屏?|prpr"),
    Meme("twist", twist, ("搓",)),
    Meme("wallpaper", wallpaper, ("墙纸",)),
    Meme("china_flag", china_flag, ("国旗",)),
    Meme("make_friend", make_friend, ("交个朋友",)),
    Meme("back_to_work", back_to_work, ("继续干活", "打工人")),
    Meme("perfect", perfect, ("完美",), r"完美的?"),
    Meme("follow", follow, ("关注",)),
    Meme("my_friend", my_friend, ("我朋友说",), r"我(?:有个)?朋友(?P<name>.*?)说"),
    Meme("paint", paint, ("这像画吗",)),
    Meme("shock", shock, ("震惊",)),
    Meme("coupon", coupon, ("兑换券",)),
    Meme("listen_music", listen_music, ("听音乐",)),
    Meme("dianzhongdian", dianzhongdian, ("典中典", "黑白草图")),
    Meme("funny_mirror", funny_mirror, ("哈哈镜",)),
    Meme("love_you", love_you, ("永远爱你",)),
    Meme("symmetric", symmetric, ("对称",)),
    Meme("safe_sense", safe_sense, ("安全感",)),
    Meme("always_like", always_like, ("我永远喜欢",), r"我?永远喜欢"),
    Meme("interview", interview, ("采访",)),
    Meme("punch", punch, ("打拳",)),
    Meme("cyan", cyan, ("群青",)),
    Meme("pound", pound, ("捣",)),
    Meme("thump", thump, ("捶",)),
    Meme("need", need, ("需要", "你可能需要")),
    Meme("cover_face", cover_face, ("捂脸",)),
    Meme("knock", knock, ("敲",)),
    Meme("garbage", garbage, ("垃圾", "垃圾桶"), r"垃圾桶?"),
    Meme("whyatme", whyatme, ("为什么@我",), r"为什么(?:@|at)我"),
    Meme("decent_kiss", decent_kiss, ("像样的亲亲",)),
    Meme("jiujiu", jiujiu, ("啾啾",)),
    Meme("suck", suck, ("吸", "嗦")),
    Meme("hammer", hammer, ("锤",)),
    Meme("tightly", tightly, ("紧贴", "紧紧贴着")),
    Meme("distracted", distracted, ("注意力涣散",)),
    Meme("anyasuki", anyasuki, ("阿尼亚喜欢",)),
    Meme("thinkwhat", thinkwhat, ("想什么",)),
    Meme("keepaway", keepaway, ("远离",)),
    Meme("marriage", marriage, ("结婚申请", "结婚登记")),
    Meme("painter", painter, ("小画家",)),
    Meme("repeat", repeat, ("复读",)),
    Meme("anti_kidnap", anti_kidnap, ("防诱拐",)),
    Meme("charpic", charpic, ("字符画",)),
    Meme("mywife", mywife, ("这是我的老婆",), r"这是(?P<ta>\S+)的(?P<name>\S+)"),
    Meme("walnutpad", walnutpad, ("胡桃平板",)),
    Meme("teach", teach, ("讲课", "敲黑板")),
    Meme("addition", addition, ("上瘾", "毒瘾发作")),
    Meme("gun", gun, ("手枪",)),
    Meme("blood_pressure", blood_pressure, ("高血压",)),
    Meme("read_book", read_book, ("看书",)),
]
