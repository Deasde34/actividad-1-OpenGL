from OpenGL.GL import *
import glfw

def dibujar():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-1.0,0.0,0.0)
    glVertex3f(0.0,1.0,0.0)
    glVertex3f(1.0,0.0,0.0)

    glEnd()
    
def main():
    width = 400
    height = 600

    if not glfw.init():
        return
    window = glfw.create_window(width, height, "mi ventana", None, None)
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    version = glGetString(GL_VERSION)
    print(version)
    while not glfw.window_should_close(window): 
        glViewport(0, 0, width, height)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #DIBUJAR
        dibujar()
        glfw.poll_events()
        glBegin(GL_LINES)
        glColor3f(1.0,0.0,0.0)
        glVertex3f(-0.7,0.0,0.0)
        glVertex3f(0.0,0.0,0.0)
        glVertex3f(0.4,-0.1,0.0)
        glVertex3f(0.35,-0.6,0.0)
        glEnd()

        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()
#ejecutar el main
if __name__ =="__main__":
    main()
