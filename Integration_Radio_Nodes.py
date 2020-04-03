file1 = open("E:\Data.txt","r") #Data File
file2 = open("E:\Batch.txt","w") #Batch file as output
newfields=[] #Variable to stare content

for data in file1:
  fields = data.split("\t")
  SNo = fields[0]
  Site = fields[1]
  Node = fields[2]
  BSC = fields[3]
  RNC = fields[4]
  IP = fields[5]
  Type = fields[6]
  newfields.append(fields)
  print(newfields)
  if "Integration" in Type:
    if "NODE" in Node:
       continue
    if "LU" in Node :
      if Node !="GU" and Node =="GLU" and Node !="GL" :
                            file2.write("cmedit create NetworkElement="+Node)
                            file2.write(" networkElementId="+Node+', neType=RadioNode, ossModelIdentity="19.Q2-R34A11",timeZone="Asia/Rangoon",ossPrefix="SubNetwork=LTE,MeContext=')
                            file2.write(Node+'" -ns=OSS_NE_DEF -v=2.0.0'+'\n')
                            file2.write("cmedit set NetworkElement="+Node+' controllingRnc='+RNC+'"NetworkElement='+Node+'"\n')
                            file2.write("cmedit create NetworkElement="+Node+',ComConnectivityInformation=1 ComConnectivityInformationId="1",snmpVersion="SNMP_V2C",snmpWriteCommunity="public",snmpReadCommunity="public",ipAddress="'+IP+'",transportProtocol="TLS",ftpTlsServerPort="9921",port="6513",snmpSecurityLevel="NO_AUTH_NO_PRIV" -namespace=COM_MED -version=1.1.0'+'\n')
                            file2.write('secadm credentials create --secureusername rbsuser --secureuserpassword "rbsuser123" --ldapuser enable -n '+Node+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',CmNodeHeartbeatSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',PmFunction=1 pmEnabled=true --force'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',FmAlarmSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',InventorySupervision=1 active=true'+'\n')
                            file2.write('cmedit action NetworkElement='+Node+',CmFunction=1 sync'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1 geographicLocationId=1 -ns=OSS_GEO -v=2.0.0'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1, GeometricPoint=1 geometricPointId=1, latitude="0",longitude="0" -ns=OSS_GEO -v=2.0.1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',CmFunction=1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',SecurityFunction=1,NetworkElementSecurity=1'+'\n')
    if "GU" in Node :
      if Node !="LU" and Node =="GLU" and Node !="GL" : 
                            file2.write('cmedit create NetworkElement='+Node+' networkElementId='+Node+', neType=RadioNode, ossModelIdentity="19.Q2-R34A11",timeZone="Asia/Rangoon",ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork='+RNC+',MeContext='+Node+'" -ns=OSS_NE_DEF -v=2.0.0'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingRnc="NetworkElement='+RNC+'"\n')
                            file2.write('cmedit create NetworkElement='+Node+',ComConnectivityInformation=1 ComConnectivityInformationId="1",snmpVersion="SNMP_V2C",snmpWriteCommunity="public",snmpReadCommunity="public",ipAddress="'+IP+'",transportProtocol="TLS",ftpTlsServerPort="9921",port="6513",snmpSecurityLevel="NO_AUTH_NO_PRIV" -namespace=COM_MED -version=1.1.0'+'\n')
                            file2.write('secadm credentials create --secureusername rbsuser --secureuserpassword "rbsuser123" --ldapuser enable -n '+Node+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',CmNodeHeartbeatSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',PmFunction=1 pmEnabled=true --force'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',FmAlarmSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',InventorySupervision=1 active=true'+'\n')
                            file2.write('cmedit action NetworkElement='+Node+',CmFunction=1 sync'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1 geographicLocationId=1 -ns=OSS_GEO -v=2.0.0'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1, GeometricPoint=1 geometricPointId=1, latitude="0",longitude="0" -ns=OSS_GEO -v=2.0.1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',CmFunction=1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',SecurityFunction=1,NetworkElementSecurity=1'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingBsc="NetworkElement='+BSC+'\n')
  if "GL" in Node :
    if Node !="GU" and Node =="GLU" and Node !="LU" :
                            file2.write('cmedit create NetworkElement='+Node+' networkElementId='+Node+', neType=RadioNode, ossModelIdentity="19.Q2-R34A11",timeZone="Asia/Rangoon",ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE,MeContext='+Node+'" -ns=OSS_NE_DEF -v=2.0.0'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingRnc="NetworkElement='+RNC+'"\n')
                            file2.write('cmedit create NetworkElement='+Node+',ComConnectivityInformation=1 ComConnectivityInformationId="1",snmpVersion="SNMP_V2C",snmpWriteCommunity="public",snmpReadCommunity="public",ipAddress="'+IP+'",transportProtocol="TLS",ftpTlsServerPort="9921",port="6513",snmpSecurityLevel="NO_AUTH_NO_PRIV" -namespace=COM_MED -version=1.1.0'+'\n')
                            file2.write('secadm credentials create --secureusername rbsuser --secureuserpassword "rbsuser123" --ldapuser enable -n '+Node+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',CmNodeHeartbeatSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',PmFunction=1 pmEnabled=true --force'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',FmAlarmSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',InventorySupervision=1 active=true'+'\n')
                            file2.write('cmedit action NetworkElement='+Node+',CmFunction=1 sync'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1 geographicLocationId=1 -ns=OSS_GEO -v=2.0.0'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1, GeometricPoint=1 geometricPointId=1, latitude="0",longitude="0" -ns=OSS_GEO -v=2.0.1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',CmFunction=1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',SecurityFunction=1,NetworkElementSecurity=1'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingBsc="NetworkElement='+BSC+'\n')
  if "GLU" in Node :
    if Node =="GU" and Node =="LU" and Node =="GL" :
                            file2.write('cmedit create NetworkElement='+Node+' networkElementId='+Node+', neType=RadioNode, ossModelIdentity="19.Q2-R34A11",timeZone="Asia/Rangoon",ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE,MeContext='+Node+'" -ns=OSS_NE_DEF -v=2.0.0'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingRnc="NetworkElement='+RNC+'"\n')
                            file2.write('cmedit create NetworkElement='+Node+',ComConnectivityInformation=1 ComConnectivityInformationId="1",snmpVersion="SNMP_V2C",snmpWriteCommunity="public",snmpReadCommunity="public",ipAddress="'+IP+'",transportProtocol="TLS",ftpTlsServerPort="9921",port="6513",snmpSecurityLevel="NO_AUTH_NO_PRIV" -namespace=COM_MED -version=1.1.0'+'\n')
                            file2.write('secadm credentials create --secureusername rbsuser --secureuserpassword "rbsuser123" --ldapuser enable -n '+Node+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',CmNodeHeartbeatSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',PmFunction=1 pmEnabled=true --force'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',FmAlarmSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',InventorySupervision=1 active=true'+'\n')
                            file2.write('cmedit action NetworkElement='+Node+',CmFunction=1 sync'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1 geographicLocationId=1 -ns=OSS_GEO -v=2.0.0'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1, GeometricPoint=1 geometricPointId=1, latitude="0",longitude="0" -ns=OSS_GEO -v=2.0.1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',CmFunction=1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',SecurityFunction=1,NetworkElementSecurity=1'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingBsc="NetworkElement='+BSC+'\n')
  if Node!="GLU" and Node !="GU" and Node !="LU" and Node !="GL" and Node!="NODE" :
                            file2.write('cmedit create NetworkElement='+Node+' networkElementId='+Node+', neType=RadioNode, ossModelIdentity="19.Q2-R34A11",timeZone="Asia/Rangoon",ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork='+RNC+',MeContext='+Node+'" -ns=OSS_NE_DEF -v=2.0.0'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingRnc="NetworkElement='+RNC+'"\n')
                            file2.write('cmedit create NetworkElement='+Node+',ComConnectivityInformation=1 ComConnectivityInformationId="1",snmpVersion="SNMP_V2C",snmpWriteCommunity="public",snmpReadCommunity="public",ipAddress="'+IP+'",transportProtocol="TLS",ftpTlsServerPort="9921",port="6513",snmpSecurityLevel="NO_AUTH_NO_PRIV" -namespace=COM_MED -version=1.1.0'+'\n')
                            file2.write('secadm credentials create --secureusername rbsuser --secureuserpassword "rbsuser123" --ldapuser enable -n '+Node+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',CmNodeHeartbeatSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',PmFunction=1 pmEnabled=true --force'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',FmAlarmSupervision=1 active=true'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+',InventorySupervision=1 active=true'+'\n')
                            file2.write('cmedit action NetworkElement='+Node+',CmFunction=1 sync'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1 geographicLocationId=1 -ns=OSS_GEO -v=2.0.0'+'\n')
                            file2.write('cmedit create NetworkElement='+Node+',GeographicLocation=1, GeometricPoint=1 geometricPointId=1, latitude="0",longitude="0" -ns=OSS_GEO -v=2.0.1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',CmFunction=1'+'\n')
                            file2.write('cmedit get NetworkElement='+Node+',SecurityFunction=1,NetworkElementSecurity=1'+'\n')
                            file2.write('cmedit set NetworkElement='+Node+' controllingBsc="NetworkElement='+BSC+'\n')

file1.close()
file2.close()
