import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptıyapıldı [DEBUG]')

@bot.command()
async def help(ctx):
    await ctx.send("Mevcut komut(lar): '.kirlilik [toprak/hava/su]'")

@bot.command()
async def kirlilik(ctx, *, pollution):
    pollutionInfoList = {
        "toprak": "Toprağın kimyasal maddelerle veya atıklarla kirlenmesidir. Toprak kirlenmesi, hava ve suları kirleten maddeler tarafından meydana getirilebilir. Örneğin, kükürt dioksit oranı yüksek olan bir atmosfer tabakasından geçen yağmur damlacıkları asit yağmuru hâlinde toprağa geçer. Toprak içine giren bu asitli sular ağaç köklerini, bitkisel ve hayvansal toprak canlılarını zarara uğratır.",
        "hava": "Atmosferde duman, toz ve saf olmayan su buharı şeklinde bulunabilecek kirleticilerin, insanlar ve diğer canlılar ile eşyaya zarar verebilecek miktarlara yükselmesi Hava kirliliği olarak nitelenmektedir. Hava kirliliğine karşı alınabilecek önlemler, kirlilik kaynağına göre (fabrika, termik santral, konutlar, taşıt araçları) çok çeşitlidir. Bu önlemler başta eğitim alınmak üzere teknik, hukuksal önlemler olmak üzere başlıca 3 grupta toplanabilir. Birçok ülkenin hava kirliliğinin sınırı vardır fakat gelişmiş ülkeler bu sınırı aşmakta ve aşmaya devam ediyor.",
        "su": "Su kirliliği, istenmeyen zararlı maddelerin, suyun niteliğini ölçülebilecek oranda bozmalarını sağlayacak miktar ve yoğunlukta suya karışma olayıdır. Konutlar, endüstri kuruluşları, termik santraller, gübreler, kimyasal mücadele ilaçları (pestisitler), tarımsal sanayi atık suları, nükleer santrallerden çıkan sıcak sular ve toprak erozyonu gibi süreçler ve maddeler su kirliliğini meydana getiren başlıca kaynaklardır. Bunların hepsi doğrudan doğruya veya dolaylı olarak canlı ve cansız varlıklara zarar vermektedir."
    }
    solutionInfoList = {
        "toprak": "Toprak kirliliğini önlemek için, kimyasal maddelerin ve atıkların toprağa karışmasını engellemek önemlidir. Tarımda organik gübreler kullanmak, endüstriyel atıkları uygun şekilde yönetmek ve çevre dostu tarım uygulamalarını teşvik etmek gibi önlemler alınabilir.",
        "hava": "Hava kirliliğini azaltmak için, fosil yakıt kullanımını azaltmak, yenilenebilir enerji kaynaklarına geçiş yapmak, toplu taşıma araçlarını kullanmak ve endüstriyel emisyonları kontrol altına almak gibi adımlar atılabilir.",
        "su": "Su kirliliğini önlemek için, atık suların arıtılması, kimyasal maddelerin su kaynaklarına karışmasının engellenmesi, tarımsal faaliyetlerde sürdürülebilir yöntemlerin kullanılması ve plastik atıkların suya atılmaması gibi önlemler alınabilir."
    }

    pollution = pollution.lower()

    if pollution in pollutionInfoList:
        await ctx.send(pollutionInfoList[pollution])
        await ctx.send(solutionInfoList[pollution])
    else:
        await ctx.send("Bu kirlilik hakkında bir bilgi yok. Lütfen, '.help' komutunu kullanın")
