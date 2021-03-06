#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None


class EntitySource:
    """
    Attributes:
     - url
     - url_id
     - site
     - site_id
     - domain
     - domain_id
     - src_type
     - download_time
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'url', None, None,),  # 1
        (2, TType.I64, 'url_id', None, None,),  # 2
        (3, TType.STRING, 'site', None, None,),  # 3
        (4, TType.I64, 'site_id', None, None,),  # 4
        (5, TType.STRING, 'domain', None, None,),  # 5
        (6, TType.I64, 'domain_id', None, None,),  # 6
        (7, TType.STRING, 'src_type', None, None,),  # 7
        (8, TType.I32, 'download_time', None, None,),  # 8
    )

    def __init__(self, url=None, url_id=None, site=None, site_id=None, domain=None, domain_id=None, src_type=None,
                 download_time=None, ):
        self.url = url
        self.url_id = url_id
        self.site = site
        self.site_id = site_id
        self.domain = domain
        self.domain_id = domain_id
        self.src_type = src_type
        self.download_time = download_time

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.url = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.url_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.site = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.site_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.domain = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.domain_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.src_type = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.download_time = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('EntitySource')
        if self.url is not None:
            oprot.writeFieldBegin('url', TType.STRING, 1)
            oprot.writeString(self.url)
            oprot.writeFieldEnd()
        if self.url_id is not None:
            oprot.writeFieldBegin('url_id', TType.I64, 2)
            oprot.writeI64(self.url_id)
            oprot.writeFieldEnd()
        if self.site is not None:
            oprot.writeFieldBegin('site', TType.STRING, 3)
            oprot.writeString(self.site)
            oprot.writeFieldEnd()
        if self.site_id is not None:
            oprot.writeFieldBegin('site_id', TType.I64, 4)
            oprot.writeI64(self.site_id)
            oprot.writeFieldEnd()
        if self.domain is not None:
            oprot.writeFieldBegin('domain', TType.STRING, 5)
            oprot.writeString(self.domain)
            oprot.writeFieldEnd()
        if self.domain_id is not None:
            oprot.writeFieldBegin('domain_id', TType.I64, 6)
            oprot.writeI64(self.domain_id)
            oprot.writeFieldEnd()
        if self.src_type is not None:
            oprot.writeFieldBegin('src_type', TType.STRING, 7)
            oprot.writeString(self.src_type)
            oprot.writeFieldEnd()
        if self.download_time is not None:
            oprot.writeFieldBegin('download_time', TType.I32, 8)
            oprot.writeI32(self.download_time)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.url)
        value = (value * 31) ^ hash(self.url_id)
        value = (value * 31) ^ hash(self.site)
        value = (value * 31) ^ hash(self.site_id)
        value = (value * 31) ^ hash(self.domain)
        value = (value * 31) ^ hash(self.domain_id)
        value = (value * 31) ^ hash(self.src_type)
        value = (value * 31) ^ hash(self.download_time)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EntityExtractorInfo:
    """
    Attributes:
     - entity_source
     - update_time
     - topic_id
     - entity_data
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'entity_source', (EntitySource, EntitySource.thrift_spec), None,),  # 1
        (2, TType.I32, 'update_time', None, None,),  # 2
        (3, TType.I32, 'topic_id', None, None,),  # 3
        (4, TType.STRING, 'entity_data', None, None,),  # 4
    )

    def __init__(self, entity_source=None, update_time=None, topic_id=None, entity_data=None, ):
        self.entity_source = entity_source
        self.update_time = update_time
        self.topic_id = topic_id
        self.entity_data = entity_data

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.entity_source = EntitySource()
                    self.entity_source.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.update_time = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.topic_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.entity_data = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('EntityExtractorInfo')
        if self.entity_source is not None:
            oprot.writeFieldBegin('entity_source', TType.STRUCT, 1)
            self.entity_source.write(oprot)
            oprot.writeFieldEnd()
        if self.update_time is not None:
            oprot.writeFieldBegin('update_time', TType.I32, 2)
            oprot.writeI32(self.update_time)
            oprot.writeFieldEnd()
        if self.topic_id is not None:
            oprot.writeFieldBegin('topic_id', TType.I32, 3)
            oprot.writeI32(self.topic_id)
            oprot.writeFieldEnd()
        if self.entity_data is not None:
            oprot.writeFieldBegin('entity_data', TType.STRING, 4)
            oprot.writeString(self.entity_data)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.entity_source)
        value = (value * 31) ^ hash(self.update_time)
        value = (value * 31) ^ hash(self.topic_id)
        value = (value * 31) ^ hash(self.entity_data)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ResultResp:
    """
    Attributes:
     - code
     - msg
     - data
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None,),  # 1
        (2, TType.STRING, 'msg', None, None,),  # 2
        (3, TType.STRING, 'data', None, None,),  # 3
    )

    def __init__(self, code=None, msg=None, data=None, ):
        self.code = code
        self.msg = msg
        self.data = data

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.msg = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.data = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ResultResp')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 2)
            oprot.writeString(self.msg)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.STRING, 3)
            oprot.writeString(self.data)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.code)
        value = (value * 31) ^ hash(self.msg)
        value = (value * 31) ^ hash(self.data)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EntityResp:
    """
    Attributes:
     - code
     - msg
     - entity_data_list
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None,),  # 1
        (2, TType.STRING, 'msg', None, None,),  # 2
        (3, TType.LIST, 'entity_data_list', (TType.STRUCT, (EntityExtractorInfo, EntityExtractorInfo.thrift_spec)),
         None,),  # 3
    )

    def __init__(self, code=None, msg=None, entity_data_list=None, ):
        self.code = code
        self.msg = msg
        self.entity_data_list = entity_data_list

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.msg = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.entity_data_list = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = EntityExtractorInfo()
                        _elem5.read(iprot)
                        self.entity_data_list.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('EntityResp')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 2)
            oprot.writeString(self.msg)
            oprot.writeFieldEnd()
        if self.entity_data_list is not None:
            oprot.writeFieldBegin('entity_data_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.entity_data_list))
            for iter6 in self.entity_data_list:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.code)
        value = (value * 31) ^ hash(self.msg)
        value = (value * 31) ^ hash(self.entity_data_list)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
