
import os,sys,re

def install(options,buildout):
    # adding maps files
    f = os.path.join(options['compile-directory'], 'Makefile.in')
    c = open(f).read() 
    for dep in 'openssl',:
        op = buildout[dep]['location']
        oplp = os.path.join(op, 'lib')
        opip = os.path.join(op, 'include')
        opl = '-L%s -Wl,-rpath -Wl,%s' % (oplp, oplp)
        opi = '-I%s' % (opip)
        if dep == 'openssl':
            opi += ' -I%s/openssl' % (opip)
        c = re.sub('APRUTIL_LDFLAGS = @APRUTIL_LDFLAGS@', 'APRUTIL_LDFLAGS = %s @APRUTIL_LDFLAGS@'  % opl,c)
        c = re.sub('APRUTIL_LIBS = @APRUTIL_LIBS@', 'APRUTIL_LIBS = %s @APRUTIL_LIBS@' % opl, c)
        c = re.sub('INCLUDES =', 'INCLUDES = %s %s' % (opi, opl), c)
    open(f, 'w').write(c)




