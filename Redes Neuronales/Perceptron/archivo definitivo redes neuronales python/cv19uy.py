class Red:
    def __init__(self):
        
        #Nota: perceptron solo desde la capa oculta hasta la salida. Las capas de entradsa referenciar solo como variables. los datos: caso de XOR es 1 y 0.
        # #Es decir solo la capa oculta realizaoperaciones 
        self.capas = 4 #Numero de capas
        self.neuronas_por_capa = [1,7,7,1] #neuronas definidas por capas
        self.entradas = [] #Array con cada salida de cada neurona del perceptron  [[1,0],[[.08912,.019238],[0.9871237]]] el subarray indica la capa y el otro la neurona
        self.pesos = [] #Pesos definidos en un array 4d [capa,[numero de neurona,[numero de peso con sus valores (j,i,random.random())]]]
        self.umbrales = []#[[numero,valor]]#cada sub array es una ca
        #[[0,0,random]] [[[],[]]]
        self.tasaAprende = 0.4 
        self.build()   #Se ejecuta el metodo que calcula todos los pesos y umbrales, les asigna un valor y determina su posicion en la red 
        
        #Para poder dibujuar
        self.x = []
        self.y = []

        #Entradas     
        self.xor =[[0.0], [0.0025575447570332483], [0.005115089514066497], [0.0076726342710997444], [0.010230179028132993], [0.01278772378516624], [0.015345268542199489], [0.017902813299232736], [0.020460358056265986], [0.023017902813299233], [0.02557544757033248], [0.028132992327365727], [0.030690537084398978], [0.03324808184143223], [0.03580562659846547], [0.03836317135549872], [0.04092071611253197], [0.043478260869565216], [0.04603580562659847], [0.04859335038363171], [0.05115089514066496], [0.05370843989769821], [0.056265984654731455], [0.058823529411764705], [0.061381074168797956], [0.0639386189258312], [0.06649616368286446], [0.06905370843989769], [0.07161125319693094], [0.0741687979539642], [0.07672634271099744], [0.0792838874680307], [0.08184143222506395], [0.08439897698209718], [0.08695652173913043], [0.08951406649616368], [0.09207161125319693], [0.09462915601023018], [0.09718670076726342], [0.09974424552429667], [0.10230179028132992], [0.10485933503836317], [0.10741687979539642], [0.10997442455242967], [0.11253196930946291], [0.11508951406649616], [0.11764705882352941], [0.12020460358056266], [0.12276214833759591], [0.12531969309462915], [0.1278772378516624], [0.13043478260869565], [0.1329923273657289], [0.13554987212276215], [0.13810741687979539], [0.14066496163682865], [0.1432225063938619], [0.14578005115089515], [0.1483375959079284], [0.15089514066496162], [0.1534526854219949], [0.15601023017902813], [0.1585677749360614], [0.16112531969309463], [0.1636828644501279], [0.16624040920716113], [0.16879795396419436], [0.17135549872122763], [0.17391304347826086], [0.17647058823529413], [0.17902813299232737], [0.1815856777493606], [0.18414322250639387], [0.1867007672634271], [0.18925831202046037], [0.1918158567774936], [0.19437340153452684], [0.1969309462915601], [0.19948849104859334], [0.2020460358056266], [0.20460358056265984], [0.2071611253196931], [0.20971867007672634], [0.21227621483375958], [0.21483375959079284], [0.21739130434782608], [0.21994884910485935], [0.22250639386189258], [0.22506393861892582], [0.22762148337595908], [0.23017902813299232], [0.23273657289002558], [0.23529411764705882], [0.23785166240409208], [0.24040920716112532], [0.24296675191815856], [0.24552429667519182], [0.24808184143222506], [0.2506393861892583], [0.2531969309462916], [0.2557544757033248], [0.25831202046035806], [0.2608695652173913], [0.26342710997442453], [0.2659846547314578], [0.26854219948849106], [0.2710997442455243], [0.27365728900255754], [0.27621483375959077], [0.27877237851662406], [0.2813299232736573], [0.28388746803069054], [0.2864450127877238], [0.289002557544757], [0.2915601023017903], [0.29411764705882354], [0.2966751918158568], [0.29923273657289], [0.30179028132992325], [0.30434782608695654], [0.3069053708439898], [0.309462915601023], [0.31202046035805625], [0.3145780051150895], [0.3171355498721228], [0.319693094629156], [0.32225063938618925], [0.3248081841432225], [0.3273657289002558], [0.329923273657289], [0.33248081841432225], [0.3350383631713555], [0.3375959079283887], [0.340153452685422], [0.34271099744245526], [0.3452685421994885], [0.34782608695652173], [0.35038363171355497], [0.35294117647058826], [0.3554987212276215], [0.35805626598465473], [0.36061381074168797], [0.3631713554987212], [0.3657289002557545], [0.36828644501278773], [0.37084398976982097], [0.3734015345268542], [0.37595907928388744], [0.37851662404092073], [0.38107416879795397], [0.3836317135549872], [0.38618925831202044], [0.3887468030690537], [0.391304347826087], [0.3938618925831202], [0.39641943734015345], [0.3989769820971867], [0.40153452685422], [0.4040920716112532], [0.40664961636828645], [0.4092071611253197], [0.4117647058823529], [0.4143222506393862], [0.41687979539641945], [0.4194373401534527], [0.4219948849104859], [0.42455242966751916], [0.42710997442455245], [0.4296675191815857], [0.4322250639386189], [0.43478260869565216], [0.4373401534526854], [0.4398976982097187], [0.4424552429667519], [0.44501278772378516], [0.4475703324808184], [0.45012787723785164], [0.45268542199488493], [0.45524296675191817], [0.4578005115089514], [0.46035805626598464], [0.4629156010230179], [0.46547314578005117], [0.4680306905370844], [0.47058823529411764], [0.4731457800511509], [0.47570332480818417], [0.4782608695652174], [0.48081841432225064], [0.4833759590792839], [0.4859335038363171], [0.4884910485933504], [0.49104859335038364], [0.4936061381074169], [0.4961636828644501], [0.49872122762148335], [0.5012787723785166], [0.5038363171355499], [0.5063938618925832], [0.5089514066496164], [0.5115089514066496], [0.5140664961636828], [0.5166240409207161], [0.5191815856777494], [0.5217391304347826], [0.5242966751918159], [0.5268542199488491], [0.5294117647058824], [0.5319693094629157], [0.5345268542199488], [0.5370843989769821], [0.5396419437340153], [0.5421994884910486], [0.5447570332480819], [0.5473145780051151], [0.5498721227621484], [0.5524296675191815], [0.5549872122762148], 
                    [0.5575447570332481], [0.5601023017902813], [0.5626598465473146], [0.5652173913043478], [0.5677749360613811], [0.5703324808184144], [0.5728900255754475], [0.5754475703324808], [0.578005115089514], [0.5805626598465473], [0.5831202046035806], [0.5856777493606138], [0.5882352941176471], [0.5907928388746803], 
                    [0.5933503836317136], [0.5959079283887468], [0.59846547314578], [0.6010230179028133], [0.6035805626598465], [0.6061381074168798], [0.6086956521739131], [0.6112531969309463], [0.6138107416879796], [0.6163682864450127], [0.618925831202046], [0.6214833759590793], [0.6240409207161125], [0.6265984654731458], [0.629156010230179], [0.6317135549872123], [0.6342710997442456], [0.6368286445012787], [0.639386189258312], [0.6419437340153452], [0.6445012787723785], [0.6470588235294118], [0.649616368286445], [0.6521739130434783], [0.6547314578005116], [0.6572890025575447], [0.659846547314578], [0.6624040920716112], [0.6649616368286445], [0.6675191815856778], [0.670076726342711], [0.6726342710997443], [0.6751918158567775], [0.6777493606138107], [0.680306905370844], [0.6828644501278772], [0.6854219948849105], [0.6879795396419437], [0.690537084398977], [0.6930946291560103], [0.6956521739130435], [0.6982097186700768], [0.7007672634271099], [0.7033248081841432], [0.7058823529411765], [0.7084398976982097], [0.710997442455243], [0.7135549872122762], [0.7161125319693095], [0.7186700767263428], [0.7212276214833759], [0.7237851662404092], [0.7263427109974424], [0.7289002557544757], [0.731457800511509], [0.7340153452685422], [0.7365728900255755], [0.7391304347826086], [0.7416879795396419], [0.7442455242966752], [0.7468030690537084], [0.7493606138107417], [0.7519181585677749], [0.7544757033248082], [0.7570332480818415], [0.7595907928388747], [0.7621483375959079], [0.7647058823529411], [0.7672634271099744], [0.7698209718670077], [0.7723785166240409], [0.7749360613810742], [0.7774936061381074], [0.7800511508951407], [0.782608695652174], [0.7851662404092071], [0.7877237851662404], [0.7902813299232737], [0.7928388746803069], [0.7953964194373402], [0.7979539641943734], [0.8005115089514067], [0.80306905370844], [0.8056265984654731], [0.8081841432225064], [0.8107416879795396], [0.8132992327365729], [0.8158567774936062], [0.8184143222506394], [0.8209718670076727], [0.8235294117647058], [0.8260869565217391], [0.8286445012787724], [0.8312020460358056], [0.8337595907928389], [0.8363171355498721], [0.8388746803069054], [0.8414322250639387], [0.8439897698209718], [0.8465473145780051], [0.8491048593350383], [0.8516624040920716], [0.8542199488491049], [0.8567774936061381], [0.8593350383631714], [0.8618925831202046], [0.8644501278772379], [0.8670076726342711], [0.8695652173913043], [0.8721227621483376], [0.8746803069053708], [0.8772378516624041], [0.8797953964194374], [0.8823529411764706], [0.8849104859335039], [0.887468030690537], [0.8900255754475703], [0.8925831202046036], [0.8951406649616368], [0.8976982097186701], [0.9002557544757033], [0.9028132992327366], [0.9053708439897699], [0.907928388746803], [0.9104859335038363], [0.9130434782608695], [0.9156010230179028], [0.9181585677749361], [0.9207161125319693], [0.9232736572890026], [0.9258312020460358], [0.928388746803069], [0.9309462915601023], [0.9335038363171355], [0.9360613810741688], [0.9386189258312021], [0.9411764705882353], [0.9437340153452686], [0.9462915601023018], [0.948849104859335], [0.9514066496163683], [0.9539641943734015], [0.9565217391304348], [0.959079283887468], [0.9616368286445013], [0.9641943734015346], [0.9667519181585678], [0.969309462915601], [0.9718670076726342], [0.9744245524296675], [0.9769820971867008], [0.979539641943734], [0.9820971867007673], [0.9846547314578005], [0.9872122762148338], [0.989769820971867], [0.9923273657289002], [0.9948849104859335], [0.9974424552429667], [1.0]]#[[0.0], [0.08458800985491378], [0.15932110594032298], [0.22474678346564456], [0.2814125376402955], [0.32986586367369264], [0.37065425677525293], [0.4043252121543933], [0.4314262250205307], [0.45250479058308196], [0.46810840405146403], [0.47878456063509384], [0.48508075554338836], [0.4875444839857645], [0.4867232411716391], [0.4831645223104291], [0.47741582261155147], [0.47002463728442306], [0.46153846153846084], [0.4525047905830817], [0.44347111962770264], [0.4349849438817404], [0.427593758554612], [0.4218450588557344], [0.41828633999452447], [0.4174650971803991], [0.4199288256227753], [0.42622502053106986], [0.4369011771146997], [0.45250479058308196], [0.47358335614563324], [0.5006843690117707], [0.5343553243909113], [0.5751437174924716], [0.6235970435258689], [0.6802627977005199], [0.7456884752258417], [0.8204215713112509], [0.9050095811661649], [1.0]]
        #Ambos array tienen que ser 2d para que sea mas facil procesar el algoritmo de backpropagation
        #SAlidas esperadas
        self.sale =[[0.0], [0.02139917695473251], [0.005761316872427984], [0.006584362139917695], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.00905349794238683], [0.0], [0.0], [0.0049382716049382715], [0.0], [0.0], [0.027160493827160494], [0.00823045267489712], [0.011522633744855968], [0.00411522633744856], [0.00411522633744856], [0.010699588477366255], [0.010699588477366255], [0.00411522633744856], [0.0032921810699588477], [0.0024691358024691358], [0.0024691358024691358], [0.0016460905349794238], [0.010699588477366255], [0.0024691358024691358], [0.00905349794238683], [0.00823045267489712], [0.006584362139917695], [0.00411522633744856], [0.0032921810699588477], [0.0049382716049382715], [0.0016460905349794238], [0.00411522633744856], [0.006584362139917695], [0.0008230452674897119], [0.0008230452674897119], [0.0024691358024691358], [0.0008230452674897119], [0.006584362139917695], [0.00905349794238683], [0.0032921810699588477], 
                    [0.00905349794238683], [0.00411522633744856], [0.014814814814814815], [0.0016460905349794238], [0.011522633744855968], [0.006584362139917695], [0.00411522633744856], [0.00411522633744856], [0.0016460905349794238], [0.0016460905349794238], [0.0008230452674897119], [0.0016460905349794238], [0.0032921810699588477], [0.0016460905349794238], [0.00905349794238683], [0.0], [0.0], [0.0008230452674897119], [0.0008230452674897119], [0.0], [0.0], [0.0], [0.0008230452674897119], [0.0], [0.0008230452674897119], [0.0], [0.0008230452674897119], [0.0024691358024691358], [0.0049382716049382715], [0.013991769547325103], [0.0049382716049382715], [0.0024691358024691358], [0.013991769547325103], [0.00411522633744856], [0.009876543209876543], [0.00411522633744856], [0.00411522633744856], [0.0024691358024691358], [0.0032921810699588477], [0.005761316872427984], [0.0032921810699588477], [0.00411522633744856], [0.0024691358024691358], [0.0008230452674897119], [0.0032921810699588477], [0.00411522633744856], [0.007407407407407408], [0.0024691358024691358], [0.006584362139917695], [0.0008230452674897119], [0.0008230452674897119], [0.0016460905349794238], [0.006584362139917695], [0.009876543209876543], [0.013991769547325103], [0.00905349794238683], [0.005761316872427984], [0.00823045267489712], [0.00823045267489712], [0.02633744855967078], [0.01728395061728395], [0.01728395061728395], [0.0205761316872428], [0.007407407407407408], [0.014814814814814815], [0.010699588477366255], [0.01646090534979424], [0.015637860082304528], [0.0049382716049382715], [0.01728395061728395], [0.011522633744855968], [0.006584362139917695], [0.007407407407407408], [0.009876543209876543], [0.00905349794238683], [0.007407407407407408], [0.005761316872427984], [0.010699588477366255], [0.014814814814814815], [0.00905349794238683], [0.01728395061728395], [0.007407407407407408], [0.01316872427983539], [0.010699588477366255], [0.012345679012345678], [0.0049382716049382715], [0.013991769547325103], [0.023045267489711935], [0.007407407407407408], [0.010699588477366255], [0.00823045267489712], [0.0049382716049382715], [0.0049382716049382715], [0.0049382716049382715], [0.0024691358024691358], [0.005761316872427984], [0.007407407407407408], [0.006584362139917695], [0.011522633744855968], [0.012345679012345678], [0.00905349794238683], [0.01316872427983539], [0.01316872427983539], [0.010699588477366255], [0.013991769547325103], [0.014814814814814815], [0.00905349794238683], [0.011522633744855968], [0.015637860082304528], [0.02551440329218107], [0.014814814814814815], [0.012345679012345678], [0.005761316872427984], [0.023045267489711935], [0.00411522633744856], [0.012345679012345678], [0.023868312757201648], [0.01646090534979424], [0.012345679012345678], [0.011522633744855968], [0.010699588477366255], [0.00823045267489712], [0.005761316872427984], [0.009876543209876543], [0.010699588477366255], [0.006584362139917695], [0.02551440329218107], [0.00823045267489712], [0.0016460905349794238], [0.018930041152263374], [0.012345679012345678], [0.012345679012345678], [0.02962962962962963], 
                    [0.0205761316872428], [0.02139917695473251], [0.00823045267489712], [0.018930041152263374], [0.023868312757201648], [0.01728395061728395], [0.0205761316872428], [0.013991769547325103], [0.022222222222222223], [0.01646090534979424], [0.019753086419753086], [0.04197530864197531], [0.023868312757201648], [0.027983539094650206], [0.04197530864197531], [0.024691358024691357], [0.024691358024691357], [0.05267489711934156], [0.03621399176954732], [0.031275720164609055], [0.048559670781893], [0.03950617283950617], [0.03950617283950617], [0.019753086419753086], [0.03621399176954732], [0.05185185185185185], [0.05185185185185185], [0.03209876543209877], [0.0345679012345679], [0.0205761316872428], [0.01316872427983539], [0.02551440329218107], [0.040329218106995884], [0.05267489711934156], [0.050205761316872426], [0.05925925925925926], [0.060082304526748974], [0.03868312757201646], [0.04938271604938271], [0.06584362139917696], [0.07818930041152264], [0.07242798353909465], [0.060905349794238686], [0.060082304526748974], [0.060905349794238686], [0.08559670781893004], [0.07242798353909465], [0.06748971193415639], [0.0823045267489712], [0.07160493827160494], [0.11193415637860082], [0.05843621399176955], [0.08888888888888889], [0.097119341563786], [0.10617283950617284], [0.15308641975308643], [0.17119341563786009], [0.17119341563786009], [0.12263374485596708], [0.1382716049382716], [0.16707818930041152], [0.19588477366255144], [0.2337448559670782], [0.1934156378600823], [0.27901234567901234], [0.17037037037037037], [0.24938271604938272], [0.24609053497942388], [0.32098765432098764], [0.3004115226337449], [0.2773662551440329], [0.43868312757201644], [0.2650205761316872], [0.3292181069958848], [0.3917695473251029], [0.45020576131687245], [0.4279835390946502], [0.5020576131687243], [0.4090534979423868], [0.362962962962963], [0.43292181069958846], [0.5860082304526749], [0.6205761316872428], [0.32181069958847736], [0.30534979423868314], [0.4213991769547325], [0.48148148148148145], [0.5407407407407407], [0.4271604938271605], [0.5300411522633744], [0.5218106995884774], [0.42962962962962964], [0.460082304526749], [0.5004115226337449], [0.5621399176954732], [0.7786008230452675], [0.6255144032921811], [0.43950617283950616], [0.522633744855967], [1.0], [0.5917695473251029], [0.7794238683127572], [0.5185185185185185], [0.8872427983539095], [0.7876543209876543], [0.5950617283950618], [0.5843621399176955], [0.4065843621399177], [0.48559670781893005], [0.7053497942386832], [0.5835390946502058], [0.9761316872427983], [0.6592592592592592], [0.551440329218107], [0.3390946502057613], [0.5300411522633744], [0.5366255144032922], [0.46255144032921813], [0.5358024691358024], [0.5366255144032922], [0.45843621399176954], [0.32592592592592595], [0.44362139917695476], [0.4510288065843621], [0.4888888888888889], [0.4148148148148148], [0.4222222222222222], [0.41069958847736626], [0.2814814814814815], [0.41646090534979424], [0.5160493827160494], [0.39423868312757204], [0.4765432098765432], [0.47818930041152263], [0.37530864197530867], [0.3736625514403292], [0.3094650205761317], [0.4090534979423868], [0.45020576131687245], [0.5234567901234568], [0.6502057613168725], [0.5382716049382716], [0.411522633744856], [0.5860082304526749], [0.6205761316872428], [0.32181069958847736], [0.30534979423868314], [0.4213991769547325], [0.48148148148148145], [0.5407407407407407], [0.4271604938271605], [0.5300411522633744], [0.5218106995884774], [0.42962962962962964], [0.460082304526749], [0.5004115226337449], [0.5621399176954732], [0.7786008230452675], [0.6255144032921811], [0.43950617283950616], [0.522633744855967], [1.0], [0.5917695473251029], [0.7794238683127572], [0.5185185185185185], [0.8872427983539095], [0.7876543209876543], [0.5950617283950618], [0.5843621399176955], [0.4065843621399177], [0.48559670781893005], [0.7053497942386832], [0.5835390946502058], [0.9761316872427983], [0.6592592592592592], [0.551440329218107], [0.3390946502057613], [0.5300411522633744], [0.5366255144032922], [0.46255144032921813], [0.5358024691358024], [0.5366255144032922], [0.45843621399176954], [0.32592592592592595], [0.44362139917695476], [0.4510288065843621], [0.4888888888888889], [0.4148148148148148], [0.4222222222222222], [0.41069958847736626], [0.2814814814814815], [0.41646090534979424], [0.5160493827160494], [0.39423868312757204], [0.4765432098765432], [0.47818930041152263], [0.37530864197530867], [0.3736625514403292], [0.3094650205761317], [0.4090534979423868], [0.45020576131687245], [0.5234567901234568], [0.6502057613168725], [0.5382716049382716], [0.411522633744856], [0.5481481481481482], [0.7440329218106996], [0.6790123456790124], [0.702880658436214], [0.6757201646090535], [0.5209876543209877], [0.49218106995884775], [0.49876543209876545]]#[[0.0], [0.025641025641025654], [0.05128205128205131], [0.07692307692307697], [0.10256410256410262], [0.12820512820512828], [0.15384615384615394], [0.1794871794871796], [0.20512820512820523], [0.23076923076923087], [0.2564102564102565], [0.2820512820512821], [0.30769230769230776], [0.3333333333333334], [0.35897435897435903], [0.3846153846153846], [0.41025641025641024], [0.4358974358974359], [0.4615384615384615], [0.48717948717948717], [0.5128205128205128], [0.5384615384615384], [0.5641025641025641], [0.5897435897435898], [0.6153846153846153], [0.641025641025641], [0.6666666666666666], [0.6923076923076923], [0.717948717948718], [0.7435897435897434], [0.7692307692307692], [0.7948717948717947], [0.8205128205128205], [0.846153846153846], [0.8717948717948718], [0.8974358974358974], [0.9230769230769231], [0.9487179487179487], [0.9743589743589745], [1.0]]
        
        
        conjuntoentradas = len(self.xor)

        for a in range(4001):
            #!!!!!Importante!!!!!!!!:para cada iiteracion se envia cada conjunto al metodo calcula salida y se ajusta los pesos correspondientes
            if a%2000==0:
                print ("------ Iteracion {} ------".format(a))
            for i in range(conjuntoentradas):
                
                self.entradas = [self.xor[i]]#Se asigna el valor de la entraa externa al perceptron
                self.calculaSalida()#Calcula la salida con foward propagation
                self.backpropagation(self.sale[i],self.xor[i])#Ajusta Pesos y Umbrales con Backpropagation

                if a%2500 == 0:
                    pass#print (self.entradas[-1][0],'<vs>',self.sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(self.sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
                    #Evalua la variacion de los resultados cada 2000 iteraciones
                if a%2000==0:#Actualiza los datos para ver como se adapta la red a la funcion inicial. Importante si se utliza el ejemplo de la funcion normalizada
                    self.actualizar_datos(self.xor[i][0],self.entradas[-1][0])
            if a%2000==0:
                self.dibujo()
            #print (self.pesos)

        #self.dibujo(conjuntoentradas)#Compara la grafica real con la obtenida 

        self.datos()#Comienza con la demostracion de lo que se aprendio
        self.demostrar()#Utiliza los pesos ajustados para calcular foward propagation y obtener una salida. Importante para predecir

    def build(self):
        
        #PESOS. Me gusta poner a en vez de k :) como variable jeje
        self.c = 0 #variable que cuenta el numero de pesos
        
        for a in range(self.capas-1):
            for j in range(self.neuronas_por_capa[a]):
                self.pesos+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
                #Para poder definir los pesos como se dijo en la linea 38
        for a in range(self.capas-1):
            if a >=self.capas:break
            for j in range(self.neuronas_por_capa[a]):
                for i in range(self.neuronas_por_capa[a+1]):
                    self.c+=1
                    self.pesos[a][j]+=[[a,j,i,random.random()]]#Asigna valores al azar

            #Umbrales
        self.u = 0 #variable que cuenta el numero de umbrales
        for a in range(1,self.capas):
            for j in range(self.neuronas_por_capa[a]):
                self.umbrales+=[[]]
        for i in range(1,self.capas):
            for j in  range(self.neuronas_por_capa[i]):
                self.u+=1
                self.umbrales[i]+=[[j,random.random()]]
        self.umbrales=self.umbrales[1:-2]#Remueve sublistas vacias
        self.umbrales = [ele for ele in self.umbrales if ele !=[]]#Remueve sublistas vacias
        self.pesos = [el for el in self.pesos if el !=[]]
        #print (self.pesos, 'PEsos')
            
    def calculaSalida(self):
        #utiliza foward propagation

        for a in  range(self.capas):
            self.entradas+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        for a in range(1,self.capas):

            for i in range(self.neuronas_por_capa[a]):       
                self.entradas[a][i] = 0

                for j in range(self.neuronas_por_capa[a-1]):

                    self.entradas[a][i] += self.entradas[a-1][j]*self.pesos[a-1][j][i][3]
                                    
                self.entradas[a][i]+=self.umbrales[a-1][i][1]

                self.entradas[a][i] = (1)/(1+(math.exp(-self.entradas[a][i])))#Sigmoide
        
        self.entradas = self.entradas[:4]#remueve algunas listas vacias


    def backpropagation(self,se,e):
        ###Todo basado en las formulas reales sin cambios significativos###


        ###PARA PESOS###
        
        #Procesa capa 4
        #variacion del error con respecto a los pesos de la capa 3
    
        for j in range(self.neuronas_por_capa[2]):
            for i in range(self.neuronas_por_capa[3]):
                yi = self.entradas[3][i]
                derror = self.entradas[2][j]*yi*(1-yi)*(-se[i]+yi)
                #print 'error', derror3
                self.pesos[2][j][i][3] = self.pesos[2][j][i][3]-(self.tasaAprende*derror)#modifica pesos. 
        
        #Procesa capa 3
        for j in range(self.neuronas_por_capa[1]):
            for k in range(self.neuronas_por_capa[2]):
                acum = 0
                for i in range(self.neuronas_por_capa[3]):
                    yi = self.entradas[3][i]
                    acum+=self.pesos[2][k][i][3]*yi*(1-yi)*(-se[i]+yi)
                derror2  = self.entradas[1][j]*self.entradas[2][k]*(1-self.entradas[2][k])*acum
                self.pesos[1][j][k][3] = self.pesos[1][j][k][3]-(self.tasaAprende*derror2)
        
        #Procesa capa 2
        for j in range(self.neuronas_por_capa[0]):
            for k in  range(self.neuronas_por_capa[1]):
                acumular = 0
                for p in range(self.neuronas_por_capa[2]):
                    acum = 0
                    for i in range(self.neuronas_por_capa[-1]):
                        yi = self.entradas[3][i]
                        acum+= self.pesos[2][p][i][3]*yi*(1-yi)*(-se[i]+yi)
                    acumular+=self.pesos[1][k][p][3]*self.entradas[2][p]*(1-self.entradas[2][p])*acum
                derror1 = e[j] * self.entradas[1][k] * (1-self.entradas[1][k]) * acumular
                self.pesos[0][j][k][3] = self.pesos[0][j][k][3]-self.tasaAprende*derror1
        
        ###Para UMBRALES###
        #Umbrales capa 4
        for i in range(self.neuronas_por_capa[3]):
            yi = self.entradas[3][i]
            derror4 = yi*(1-yi)*(-se[i]+yi)
            self.umbrales[2][i][1] = self.umbrales[2][i][1]-self.tasaAprende*derror4

        #Umbrales capa 3

        for k in range(self.neuronas_por_capa[2]):
            acum = 0
            for i in range(self.neuronas_por_capa[3]):
                yi = self.entradas[3][i]
                acum+=self.pesos[2][k][i][-1]*yi*(1-yi)*(-se[i]+yi)
            derror3 = self.entradas[2][k]*(1-self.entradas[2][k])*acum
            self.umbrales[1][k][1] = self.umbrales[1][k][1]-self.tasaAprende*derror3


        #Umbrales capa 2
        for k in range(self.neuronas_por_capa[1]):
            acumular = 0
            for p in range(self.neuronas_por_capa[2]):
                acum = 0
                for i in range(self.neuronas_por_capa[3]):
                    acum+=self.pesos[2][p][i][3]*yi*(1-yi)*(-se[i]+yi)
                acumular+=self.pesos[1][k][p][3]*self.entradas[2][p]*(1-self.entradas[2][p])*acum
            derror2 = self.entradas[1][k]*(1-self.entradas[1][k])*acumular
            self.umbrales[0][k][1] = self.umbrales[0][k][1]-self.tasaAprende*derror2
            #print self.umbrales[0][k][1], 'U(1)'

    def datos(self):
        fin = '\n\n'+colorama.Fore.LIGHTYELLOW_EX+'***'+colorama.Fore.LIGHTGREEN_EX+'Entrenamiento completado'+colorama.Fore.LIGHTYELLOW_EX+'***'
        folder = os.path.dirname(os.path.abspath(__file__))
        file1 = os.path.join(folder,'entrenamiento.txt')
        umbrales = '\n\nTotal Umbrales: {} --> {} \n'.format(self.u,self.umbrales)
        pesos = '\n\nTotal Pesos: {} --> {}\n '.format(self.c,self.pesos)
        for a in fin:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.062)

        time.sleep(1)
        print (colorama.Fore.LIGHTBLUE_EX+'\ndatos guardados en',os.getcwd(),'/entrenamiento.txt')
        file1 = open('entrenamiento.txt','w')
        file1.write(umbrales)
        file1.write(pesos)
        print (umbrales,'\n\n\n\n\n\n\n\'',pesos,'\n\n\n')
        file1.close()

        

    def demostrar(self):
        print ('\n')
        for dm in colorama.Fore.RED+'Demostracion':
            sys.stdout.write(dm)
            sys.stdout.flush()
            time.sleep(0.062)
        print (colorama.Fore.WHITE +'\n')
        centradas = input('Conjunto de entradas: ')
        try:int(centradas)
        except Exception:print (colorama.Fore.LIGHTYELLOW_EX+'Wachin, tenes que poner un numero bo\n\n')

    
        for a in range(int(centradas)):
            self.entradas = []
            c = []

            for b in range(self.neuronas_por_capa[0]):
                n_entrada = input('Entrada '+str(b)+': ')
                c.append(float(n_entrada))
            self.entradas += [c]
            print (self.salida_nueva())
            
          
        


    def salida_nueva(self):
        for a in  range(self.capas):
            self.entradas+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        for a in range(1,self.capas):
   
            for i in range(self.neuronas_por_capa[a]):       
                self.entradas[a][i] = 0
                for j in range(self.neuronas_por_capa[a-1]):

                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    self.entradas[a][i] += self.entradas[a-1][j]*self.pesos[a-1][j][i][3]
                                    
                self.entradas[a][i]=self.entradas[a][i]+self.umbrales[a-1][i][1]

                self.entradas[a][i] = (1)/(1+(math.exp(-self.entradas[a][i])))
        
        self.entradas = self.entradas[:4]       
        return self.entradas[-1][0]
    
    def actualizar_datos(self,x,y):


        self.x+=[x]#actualiza datos x
        self.y+=[y]#actualiza datos ys
    
    def dibujo(self):
        #print (self.x,self.y)
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.clear()
        ax1.plot(self.x,self.y,color = 'red',marker = 'o')#funcion obtenida
        plt.plot(self.xor,self.sale,color = 'blue',label = 'Original')#funcion original
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')            
        plt.show(block = False)
        self.x = []
        self.y = []


if __name__=='__main__':
    Perceptron()#No c pero creo que aytuda a mejorar la rapidez del programa