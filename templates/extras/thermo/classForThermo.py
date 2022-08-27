
	def findEnth(compound):
		if (compound.lower() == "ag(s)"):
			return Elements.ags.getEnth()
		elif (compound.lower() == "ag2so4(aq)"):
			return Elements.agso.getEnth()
		elif (compound.lower() == "br2(l)"):
			return Elements.br2.getEnth()
		elif (compound.lower() == "co2(g)"):
			return Elements.co2.getEnth()
		elif (compound.lower() == "cl2(g)"):
			return Elements.cl2.getEnth()
		elif (compound.lower() == "cacl2(aq)"):
			return Elements.cacl.getEnth()
		elif (compound.lower() == "ca(oh)2(s)"):
			return Elements.caoh.getEnth()
		elif (compound.lower() == "cu(s)"):
			return Elements.cus.getEnth()
		elif (compound.lower() == "cu(no3)2(aq)"):
			return Elements.cuno3.getEnth()
		elif (compound.lower() == "cuso4(aq)"):
			return Elements.cuso.getEnth()
		elif (compound.lower() == "h2(g)"):
			return Elements.h2.getEnth()
		elif (compound.lower() == "hbr(g)"):
			return Elements.hbr.getEnth()
		elif (compound.lower() == "hcl(s)"):
			return Elements.hcls.getEnth()
		elif (compound.lower() == "hcl(aq)"):
			return Elements.hcla.getEnth()
		elif (compound.lower() == "hi(g)"):
			return Elements.hi.getEnth()
		elif (compound.lower() == "hno2(aq)"):
			return Elements.hno2.getEnth()
		elif (compound.lower() == "hno3(aq)"):
			return Elements.hno3.getEnth()
		elif (compound.lower() == "h2o(l)"):
			return Elements.h2o.getEnth()
		elif (compound.lower() == "h2so4(l)"):
			return Elements.hso.getEnth()
		elif (compound.lower() == "i2(s)"):
			return Elements.i2.getEnth()
		elif (compound.lower() == "kbr(s)"):
			return Elements.kbr.getEnth()
		elif (compound.lower() == "kcl(aq)"):
			return Elements.kcl.getEnth()
		elif (compound.lower() == "k2so4(aq)"):
			return Elements.kso.getEnth()
		elif (compound.lower() == "mg(s)"):
			return Elements.mgs.getEnth()
		elif (compound.lower() == "mg3n2(s)"):
			return Elements.mgn.getEnth()
		elif (compound.lower() == "mg(no3)2"):
			return Elements.mgno.getEnth()
		elif (compound.lower() == "mg(oh)2"):
			return Elements.mgoh.getEnth()
		elif (compound.lower() == "n2(g)"):
			return Elements.n2.getEnth()
		elif (compound.lower() == "nh3(g)"):
			return Elements.nh3.getEnth()
		elif (compound.lower() == "nh4cl(aq)"):
			return Elements.nhcl.getEnth()
		elif (compound.lower() == "nh4no2(s)"):
			return Elements.nhno2.getEnth()
		elif (compound.lower() == "nh4no3(s)"):
			return Elements.nhno3.getEnth()
		elif (compound.lower() == "n2o(g)"):
			return Elements.n2o.getEnth()
		elif (compound.lower() == "no(g)"):
			return Elements.nog.getEnth()
		elif (compound.lower() == "no2(g)"):
			return Elements.no2.getEnth()
		elif (compound.lower() == "n2o5(g)"):
			return Elements.n2o5.getEnth()
		elif (compound.lower() == "nacl(s)"):
			return Elements.nacls.getEnth()
		elif (compound.lower() == "nacl(aq)"):
			return Elements.nacla.getEnth()
		elif (compound.lower() == "nano3(aq)"):
			return Elements.nano.getEnth()
		elif (compound.lower() == "naoh(aq)"):
			return Elements.naoh.getEnth()
		elif (compound.lower() == "na2so4(aq)"):
			return Elements.naso.getEnth()
		elif (compound.lower() == "o2(g)"):
			return Elements.o2.getEnth()
		elif (compound.lower() == "sio2(s)"):
			return Elements.sio.getEnth()
		elif (compound.lower() == "sn(s)"):
			return Elements.sns.getEnth()
		elif (compound.lower() == "sno2(s)"):
			return Elements.sno.getEnth()
		elif (compound.lower() == "zn(s)"):
			return Elements.zns.getEnth()
		elif (compound.lower() == "zn(oh)2(s)"):
			return Elements.znoh.getEnth()
		elif (compound.lower() == "zn(no3)2(aq)"):
			return Elements.znno.getEnth()
		else:
			return 0

	def findEntr(compound):
		if (compound.lower() == "ag(s)"):
			return Elements.ags.getEntr()
		elif (compound.lower() == "ag2so4(aq)"):
			return Elements.agso.getEntr()
		elif (compound.lower() == "br2(l)"):
			return Elements.br2.getEntr()
		elif (compound.lower() == "co2(g)"):
			return Elements.co2.getEntr()
		elif (compound.lower() == "cl2(g)"):
			return Elements.cl2.getEntr()
		elif (compound.lower() == "cacl2(aq)"):
			return Elements.cacl.getEntr()
		elif (compound.lower() == "ca(oh)2(s)"):
			return Elements.caoh.getEntr()
		elif (compound.lower() == "cu(s)"):
			return Elements.cus.getEntr()
		elif (compound.lower() == "cu(no3)2(aq)"):
			return Elements.cuno3.getEntr()
		elif (compound.lower() == "cuso4(aq)"):
			return Elements.cuso.getEntr()
		elif (compound.lower() == "h2(g)"):
			return Elements.h2.getEntr()
		elif (compound.lower() == "hbr(g)"):
			return Elements.hbr.getEntr()
		elif (compound.lower() == "hcl(s)"):
			return Elements.hcls.getEntr()
		elif (compound.lower() == "hcl(aq)"):
			return Elements.hcla.getEntr()
		elif (compound.lower() == "hi(g)"):
			return Elements.hi.getEntr()
		elif (compound.lower() == "hno2(aq)"):
			return Elements.hno2.getEntr()
		elif (compound.lower() == "hno3(aq)"):
			return Elements.hno3.getEntr()
		elif (compound.lower() == "h2o(l)"):
			return Elements.h2o.getEntr()
		elif (compound.lower() == "h2so4(l)"):
			return Elements.hso.getEntr()
		elif (compound.lower() == "i2(s)"):
			return Elements.i2.getEntr()
		elif (compound.lower() == "kbr(s)"):
			return Elements.kbr.getEntr()
		elif (compound.lower() == "kcl(aq)"):
			return Elements.kcl.getEntr()
		elif (compound.lower() == "k2so4(aq)"):
			return Elements.kso.getEntr()
		elif (compound.lower() == "mg(s)"):
			return Elements.mgs.getEntr()
		elif (compound.lower() == "mg3n2(s)"):
			return Elements.mgn.getEntr()
		elif (compound.lower() == "mg(no3)2"):
			return Elements.mgno.getEntr()
		elif (compound.lower() == "mg(oh)2"):
			return Elements.mgoh.getEntr()
		elif (compound.lower() == "n2(g)"):
			return Elements.n2.getEntr()
		elif (compound.lower() == "nh3(g)"):
			return Elements.nh3.getEntr()
		elif (compound.lower() == "nh4cl(aq)"):
			return Elements.nhcl.getEntr()
		elif (compound.lower() == "nh4no2(s)"):
			return Elements.nhno2.getEntr()
		elif (compound.lower() == "nh4no3(s)"):
			return Elements.nhno3.getEntr()
		elif (compound.lower() == "n2o(g)"):
			return Elements.n2o.getEntr()
		elif (compound.lower() == "no(g)"):
			return Elements.nog.getEntr()
		elif (compound.lower() == "no2(g)"):
			return Elements.no2.getEntr()
		elif (compound.lower() == "n2o5(g)"):
			return Elements.n2o5.getEntr()
		elif (compound.lower() == "nacl(s)"):
			return Elements.nacls.getEntr()
		elif (compound.lower() == "nacl(aq)"):
			return Elements.nacla.getEntr()
		elif (compound.lower() == "nano3(aq)"):
			return Elements.nano.getEntr()
		elif (compound.lower() == "naoh(aq)"):
			return Elements.naoh.getEntr()
		elif (compound.lower() == "na2so4(aq)"):
			return Elements.naso.getEntr()
		elif (compound.lower() == "o2(g)"):
			return Elements.o2.getEntr()
		elif (compound.lower() == "sio2(s)"):
			return Elements.sio.getEntr()
		elif (compound.lower() == "sn(s)"):
			return Elements.sns.getEntr()
		elif (compound.lower() == "sno2(s)"):
			return Elements.sno.getEntr()
		elif (compound.lower() == "zn(s)"):
			return Elements.zns.getEntr()
		elif (compound.lower() == "zn(oh)2(s)"):
			return Elements.znoh.getEntr()
		elif (compound.lower() == "zn(no3)2(aq)"):
			return Elements.znno.getEntr()
		else:
			return 0

	def findGibbs(compound):
		if (compound.lower() == "ag(s)"):
			return Elements.ags.getGibbs()
		elif (compound.lower() == "ag2so4(aq)"):
			return Elements.agso.getGibbs()
		elif (compound.lower() == "br2(l)"):
			return Elements.br2.getGibbs()
		elif (compound.lower() == "co2(g)"):
			return Elements.co2.getGibbs()
		elif (compound.lower() == "cl2(g)"):
			return Elements.cl2.getGibbs()
		elif (compound.lower() == "cacl2(aq)"):
			return Elements.cacl.getGibbs()
		elif (compound.lower() == "ca(oh)2(s)"):
			return Elements.caoh.getGibbs()
		elif (compound.lower() == "cu(s)"):
			return Elements.cus.getGibbs()
		elif (compound.lower() == "cu(no3)2(aq)"):
			return Elements.cuno3.getGibbs()
		elif (compound.lower() == "cuso4(aq)"):
			return Elements.cuso.getGibbs()
		elif (compound.lower() == "h2(g)"):
			return Elements.h2.getGibbs()
		elif (compound.lower() == "hbr(g)"):
			return Elements.hbr.getGibbs()
		elif (compound.lower() == "hcl(s)"):
			return Elements.hcls.getGibbs()
		elif (compound.lower() == "hcl(aq)"):
			return Elements.hcla.getGibbs()
		elif (compound.lower() == "hi(g)"):
			return Elements.hi.getGibbs()
		elif (compound.lower() == "hno2(aq)"):
			return Elements.hno2.getGibbs()
		elif (compound.lower() == "hno3(aq)"):
			return Elements.hno3.getGibbs()
		elif (compound.lower() == "h2o(l)"):
			return Elements.h2o.getGibbs()
		elif (compound.lower() == "h2so4(l)"):
			return Elements.hso.getGibbs()
		elif (compound.lower() == "i2(s)"):
			return Elements.i2.getGibbs()
		elif (compound.lower() == "kbr(s)"):
			return Elements.kbr.getGibbs()
		elif (compound.lower() == "kcl(aq)"):
			return Elements.kcl.getGibbs()
		elif (compound.lower() == "k2so4(aq)"):
			return Elements.kso.getGibbs()
		elif (compound.lower() == "mg(s)"):
			return Elements.mgs.getGibbs()
		elif (compound.lower() == "mg3n2(s)"):
			return Elements.mgn.getGibbs()
		elif (compound.lower() == "mg(no3)2"):
			return Elements.mgno.getGibbs()
		elif (compound.lower() == "mg(oh)2"):
			return Elements.mgoh.getGibbs()
		elif (compound.lower() == "n2(g)"):
			return Elements.n2.getGibbs()
		elif (compound.lower() == "nh3(g)"):
			return Elements.nh3.getGibbs()
		elif (compound.lower() == "nh4cl(aq)"):
			return Elements.nhcl.getGibbs()
		elif (compound.lower() == "nh4no2(s)"):
			return Elements.nhno2.getGibbs()
		elif (compound.lower() == "nh4no3(s)"):
			return Elements.nhno3.getGibbs()
		elif (compound.lower() == "n2o(g)"):
			return Elements.n2o.getGibbs()
		elif (compound.lower() == "no(g)"):
			return Elements.nog.getGibbs()
		elif (compound.lower() == "no2(g)"):
			return Elements.no2.getGibbs()
		elif (compound.lower() == "n2o5(g)"):
			return Elements.n2o5.getGibbs()
		elif (compound.lower() == "nacl(s)"):
			return Elements.nacls.getGibbs()
		elif (compound.lower() == "nacl(aq)"):
			return Elements.nacla.getGibbs()
		elif (compound.lower() == "nano3(aq)"):
			return Elements.nano.getGibbs()
		elif (compound.lower() == "naoh(aq)"):
			return Elements.naoh.getGibbs()
		elif (compound.lower() == "na2so4(aq)"):
			return Elements.naso.getGibbs()
		elif (compound.lower() == "o2(g)"):
			return Elements.o2.getGibbs()
		elif (compound.lower() == "sio2(s)"):
			return Elements.sio.getGibbs()
		elif (compound.lower() == "sn(s)"):
			return Elements.sns.getGibbs()
		elif (compound.lower() == "sno2(s)"):
			return Elements.sno.getGibbs()
		elif (compound.lower() == "zn(s)"):
			return Elements.zns.getGibbs()
		elif (compound.lower() == "zn(oh)2(s)"):
			return Elements.znoh.getGibbs()
		elif (compound.lower() == "zn(no3)2(aq)"):
			return Elements.znno.getGibbs()
		else:
			return 0