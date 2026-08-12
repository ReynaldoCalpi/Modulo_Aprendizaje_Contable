import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="ContaGo SV - Contabilidad desde Cero",
    page_icon="📊",
    layout="centered"
)

# Inicializar estado de sesión para el progreso del usuario
if "module_1_passed" not in st.session_state:
    st.session_state.module_1_passed = False
if "module_2_passed" not in st.session_state:
    st.session_state.module_2_passed = False

# ==========================================
# MENÚ LATERAL (SIDEBAR)
# ==========================================
st.sidebar.title("📊 ContaGo SV")
st.sidebar.markdown("**Contabilidad y Tributación - El Salvador**")
st.sidebar.markdown("---")

menu_options = [
    "🏠 Inicio", 
    "📚 Módulo 1: Contabilidad al Grano", 
    "💼 Módulo 2: Ley Laboral", 
    "🏛️ Módulo 3: Impuestos DGII"
]
choice = st.sidebar.selectbox("Selecciona una sección:", menu_options)

# Cálculo de progreso dinámico (3 módulos en total)
completed_modules = sum([st.session_state.module_1_passed, st.session_state.module_2_passed])
progress = int((completed_modules / 3) * 100)

st.sidebar.markdown("---")
st.sidebar.text(f"Progreso General: {progress}%")
st.sidebar.progress(progress)


# ==========================================
# CONTENIDO DE LA APLICACIÓN
# ==========================================

if choice == "🏠 Inicio":
    st.title("Bienvenido a ContaGo SV 🚀")
    st.markdown("""
    Aprende contabilidad financiera, legislación laboral y fiscalidad de **El Salvador** de forma interactiva, 
    directa al grano y sin rodeos innecesarios.
    
    ### ¿Cómo funciona?
    1. **La Píldora:** Historia, teoría esencial y los 20 conceptos clave explicados sin aburrir.
    2. **El Laboratorio:** Simuladores y clasificadores interactivos.
    3. **El Reto:** Cuestionarios prácticos para validar tu aprendizaje y desbloquear contenidos.
    
    *Utiliza el menú lateral para empezar.*
    """)

elif choice == "📚 Módulo 1: Contabilidad al Grano":
    st.title("Módulo 1: Fundamentos y Lógica Contable")
    st.markdown("Comprende la contabilidad desde sus orígenes históricos hasta dominar los **20 conceptos básicos fundamentales** de todo contador.")
    
    tab1, tab2, tab3 = st.tabs(["📖 Historia y 20 Conceptos", "🧮 Laboratorio: Clasificador", "❓ El Reto"])
    
    with tab1:
        st.subheader("🏛️ Breve Historia y Bases de la Contabilidad")
        
        st.image(
            "Imagen 1.png", 
            caption="Retrato de Luca Pacioli (1494), considerado el padre de la contabilidad moderna.",
            width=300
        )
        
        st.markdown("""
        ### 1. Un vistazo al pasado (De los mercaderes a Luca Pacioli)
        La contabilidad nació por una necesidad humana básica: **llevar cuentas claras**.
        * **Los Inicios:** Las civilizaciones antiguas (sumerios y romanos) usaban tablillas y papiros para registrar cosechas, tributos e inventarios de mercancías.
        * **El gran hito (1494):** El fraile franciscano y matemático **Luca Pacioli** publicó el libro *Summa de arithmetica*, donde formalizó y documentó por primera vez el **Sistema de la Partida Doble** que usaban los mercaderes en Venecia. ¡La regla de oro de que *"no hay deudor sin acreedor"* nació ahí!

        ### 2. Los 20 Conceptos Básicos que Todo Contador Debe Dominar
        """)
        
        st.markdown("""
        1. **Entidad Económica:** El negocio y sus dueños son personas completamente separadas. Las finanzas de la empresa jamás se mezclan con los gastos personales o familiares.
        2. **Negocio en Marcha:** Se asume que la empresa continuará operando de forma indefinida en el futuro previsible, a menos que existan evidencias de lo contrario.
        3. **Devengado:** Los ingresos y gastos se registran **cuando ocurren y se adquiere el compromiso comercial** (independientemente de si ya se pagó o se cobró en efectivo).
        4. **Dualidad Económica (Partida Doble):** Toda transacción económica tiene un origen (de dónde viene el recurso) y una aplicación (en qué se usa o invierte).
        5. **Moneda de Cuenta:** En el contexto de El Salvador, todas las operaciones financieras deben registrarse utilizando la moneda de curso legal oficial, el dólar estadounidense (USD).
        6. **Período Contable:** El tiempo convencional (usualmente del 1 de enero al 31 de diciembre) en el que se mide el rendimiento financiero y el resultado de las operaciones.
        7. **Sustancia Económica:** Las transacciones y eventos económicos deben registrarse de acuerdo con su realidad financiera y no solo por su forma legal.
        8. **Asociación de Costos y Gastos con Ingresos:** Todos los costos y gastos de un período deben identificarse con los ingresos que generaron en ese mismo lapso.
        9. **Valuación (Costo Histórico):** Los hechos económicos se registran originalmente a base de costos o valores de intercambio reales (históricos).
        10. **Importancia Relativa (Materialidad):** Los errores o revelaciones de baja cuantía que no alteren la decisión del usuario no requieren tratamiento complejo.
        11. **Prudencia (Conservatismo):** Ante la incertidumbre, se debe optar por registrar los activos y utilidades de manera moderada, pero anticipar las pérdidas o pasivos probables.
        12. **Consistencia o Uniformidad:** Las políticas y métodos contables deben mantenerse estables a lo largo del tiempo para permitir comparabilidad financiera.
        13. **Revelación Suficiente:** Los estados financieros deben incluir toda la información clara y necesaria para que los usuarios tomen decisiones informadas.
        14. **Activo:** Recurso económico presente controlado por la entidad, derivado de sucesos pasados, del cual se espera obtener beneficios económicos.
        15. **Pasivo:** Obligación presente de la entidad, surgida de sucesos pasados, cuya cancelación se espera que produzca una salida de recursos.
        16. **Patrimonio Neto:** La parte residual de los activos de la entidad, una vez deducidos todos sus pasivos (capital de los dueños).
        17. **Ingresos:** Incrementos en los beneficios económicos durante el período contable que aumentan el patrimonio (diferentes a los aportes de los socios).
        18. **Gastos:** Decrementos en los beneficios económicos durante el período contable que disminuyen el patrimonio (diferentes a los retiros de los socios).
        19. **Contabilidad Financiera:** Sistema orientado a proveer información histórica y general a usuarios externos (bancos, socios, inversionistas).
        20. **Contabilidad Fiscal:** Sistema enfocado en el cumplimiento de las normativas de tributación y control ante las entidades de gobierno (como la DGII en El Salvador).
        """)

        st.markdown("### La Ecuación Contable Fundamental:")
        st.markdown(
            r"$$\text{Activo} = \text{Pasivo} + \text{Patrimonio}$$",
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        st.markdown("### 🎥 Vídeo de apoyo:")
        st.video("https://www.youtube.com/watch?v=H9gzvXdVerc")

    with tab2:
        st.subheader("🧮 Laboratorio: Clasifica la Cuenta")
        st.markdown("Pon a prueba tu intuición comercial. Selecciona a qué categoría pertenece cada elemento típico de una empresa salvadoreña:")
        
        item_ejemplo = st.selectbox(
            "¿A qué categoría pertenece un **Vehículo de reparto** comprado para la empresa?",
            ("Selecciona una opción...", "Activo (Bien/Derecho)", "Pasivo (Deuda)", "Patrimonio (Capital de los dueños)")
        )
        
        if item_ejemplo == "Activo (Bien/Derecho)":
            st.success("¡Correcto! Un vehículo de reparto es un bien físico propiedad de la empresa, por lo tanto es un Activo.")
        elif item_ejemplo != "Selecciona una opción...":
            st.error("Incorrecto. Piensa que el vehículo le pertenece a la empresa y le genera valor económico (es un bien).")
            
        st.markdown("---")
        st.markdown("### Tipos de Contabilidad aplicados en El Salvador:")
        st.markdown("""
        1. **Contabilidad Financiera:** Evalúa la salud general del negocio para socios, bancos y terceros.
        2. **Contabilidad Fiscal (Tributaria):** Enfocada estrictamente en cumplir con las obligaciones formales y sustantivas ante el **Ministerio de Hacienda (DGII)**.
        """)

    with tab3:
        st.subheader("Cuestionario de Validación - Módulo 1")
        st.markdown("Demuestra que dominas los fundamentos ampliados para desbloquear el módulo de Ley Laboral.")
        
        answer = st.radio(
            "Según los conceptos fundamentales de la contabilidad moderna, ¿a qué se le atribuye la formalización del método de la Partida Doble en 1494?",
            (
                "Adam Smith",
                "Luca Pacioli",
                "El Ministerio de Hacienda"
            ),
            index=None
        )
        
        if st.button("Validar Respuesta Módulo 1"):
            if answer == "Luca Pacioli":
                st.success("¡Excelente! Luca Pacioli sentó las bases de la contabilidad moderna. ¡Módulo 1 superado y desbloqueado!")
                st.session_state.module_1_passed = True
            elif answer is None:
                st.warning("Por favor, selecciona una opción antes de validar.")
            else:
                st.error("Incorrecto. Recuerda que el fraile franciscano Luca Pacioli es considerado el padre de la contabilidad.")

elif choice == "💼 Módulo 2: Ley Laboral":
    st.title("Módulo 2: Ley Laboral y Planillas (El Salvador)")
    
    if not st.session_state.module_1_passed:
        st.warning("🔒 Este módulo está bloqueado. Debes completar y aprobar el **Módulo 1** en la pestaña anterior primero.")
    else:
        tab1, tab2, tab3 = st.tabs(["📖 La Píldora", "🧮 Laboratorio de Planilla", "❓ El Reto"])
        
        with tab1:
            st.subheader("Deducciones Obligatorias del Empleado")
            st.markdown("""
            Todo salario formal en El Salvador sufre dos retenciones legales básicas directas del empleado:
            
            *   **AFP (Administradora de Fondos de Pensiones):** Se descuenta el **7.25%** del salario bruto total sin límite máximo.
            *   **ISSS (Instituto Salvadoreño del Seguro Social):** Se descuenta el **3.00%**, pero ojo: tiene un **tope máximo de retención basado en un sueldo de $1,000.00** (es decir, la retención máxima de ISSS por ley es de $30.00, aunque el empleado gane más de $1,000).
            """)
            
        with tab2:
            st.subheader("Calculadora de Retenciones (Cálculo Rápido)")
            st.markdown("Ingresa un salario bruto mensual para calcular los descuentos de ley y el salario líquido:")
            
            salario_bruto = st.number_input("Salario Bruto Mensual ($)", min_value=0.0, value=650.0, step=25.0)
            
            afp = salario_bruto * 0.0725
            base_isss = min(salario_bruto, 1000.0)
            isss = base_isss * 0.03
            salario_liquido = salario_bruto - (afp + isss)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Descuento AFP (7.25%)", value=f"${afp:,.2f}")
                st.metric(label="Descuento ISSS (3%)", value=f"${isss:,.2f}")
            with col2:
                st.markdown("### Resumen:")
                st.metric(label="Total Deducciones", value=f"${(afp + isss):,.2f}")
                st.metric(label="Salario Líquido a Recibir", value=f"${salario_liquido:,.2f}")

        with tab3:
            st.subheader("Cuestionario de Validación - Ley Laboral")
            st.markdown("Valida tus conocimientos para avanzar al módulo de impuestos.")
            
            answer_m2 = st.radio(
                "¿Cuál es el porcentaje de retención laboral obligatorio destinado al fondo de pensiones (AFP) en El Salvador?",
                (
                    "3.00%",
                    "7.25%",
                    "10.00%"
                ),
                index=None
            )
            
            if st.button("Validar Respuesta Módulo 2"):
                if answer_m2 == "7.25%":
                    st.success("¡Correcto! El 7.25% corresponde a la AFP. ¡Módulo 2 superado!")
                    st.session_state.module_2_passed = True
                elif answer_m2 is None:
                    st.warning("Selecciona una opción para continuar.")
                else:
                    st.error("Incorrecto. Recuerda que el 3% es para el ISSS y el 7.25% para la AFP.")

elif choice == "🏛️ Módulo 3: Impuestos DGII":
    st.title("Módulo 3: Tributación y DGII (El Salvador)")
    
    if not st.session_state.module_2_passed:
        st.warning("🔒 Este módulo está bloqueado. Debes completar y aprobar el **Módulo 2** primero.")
    else:
        st.success("¡Bienvenido al último módulo! Aquí abordaremos el IVA (13%) y el Pago a Cuenta.")
